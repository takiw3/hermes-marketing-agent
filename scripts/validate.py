#!/usr/bin/env python3
"""Repository validation for the marketing profile distribution.

Runs every deterministic check CI enforces. Exit 0 = clean, 1 = findings.
Requires Python 3.11+ and PyYAML. Run from anywhere:

    python3 scripts/validate.py            # working tree
    python3 scripts/validate.py --history  # also scan git history for secrets
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML is required: python3 -m pip install pyyaml", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- constants

PROFILE_ID = "marketing"
LICENSE_ID = "MIT"
COPYRIGHT_LINE = "Copyright (c) 2026 TakiGPT AI Inc."
GITHUB_SLUG = "takiw3/hermes-marketing-agent"
# Split so this file never matches its own containment scan.
COMMUNITY_URL = "skool.com/" + "agenticaiacademy"

INSTALL_CMD = f"hermes profile install github.com/{GITHUB_SLUG} --alias"
INSTALL_CMD_YES = f"hermes profile install github.com/{GITHUB_SLUG} --alias --yes"
CHAT_CMD = f"hermes -p {PROFILE_ID} chat"
UPDATE_CMD = f"hermes profile update {PROFILE_ID}"
REMOVE_CMD = f"hermes profile delete {PROFILE_ID}"
KANBAN_CMD_FRAGMENT = f"--assignee {PROFILE_ID}"

SKILLS = [
    "marketing-intake-and-routing",
    "marketing-strategy",
    "brand-voice-analysis",
    "customer-and-offer-research",
    "conversion-copywriting",
    "email-sequences",
    "social-content-calendar",
    "social-performance-analysis",
    "social-carousel-creation",
    "social-script-creation",
    "paid-ad-campaigns",
    "funnel-analysis",
    "competitor-intelligence",
    "website-cro-analysis",
    "measurement-and-experimentation",
    "marketing-reporting",
    "weekly-marketing-review",
]

REQUIRED_FILES = [
    "distribution.yaml",
    "profile.yaml",
    "SOUL.md",
    "config.yaml",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".gitignore",
    ".github/workflows/ci.yml",
    "docs/architecture.md",
    "docs/onboarding.md",
    "docs/chief-of-staff-handoff.md",
    "docs/safety-and-approvals.md",
    "docs/evals.md",
    "templates/handoff-result.md",
    "templates/task-brief.md",
    "templates/approval-request.md",
    "templates/business-profile.md",
    "scripts/validate.py",
    "scripts/test_install.sh",
    "scripts/run_evals.py",
    "evals/README.md",
    "examples/README.md",
] + [f"skills/marketing-core/{s}/SKILL.md" for s in SKILLS]

# Frontmatter contract, verified against the Hermes skill loader at release
# v2026.8.19 (0.20.5): loader hard-requires name (<=64) + description
# (<=1024) + non-empty body, file <=100k chars; version/author/license are
# authoring conventions this repo enforces; tags and related_skills live
# under `metadata.hermes.`, never top-level.
FRONTMATTER_REQUIRED = ["name", "description", "version", "author", "license"]
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_SKILL_CONTENT_CHARS = 100_000

# The exact runtime allowlist the manifest may own (entries compared after
# stripping surrounding slashes, as the Hermes installer does). Anything
# else in distribution_owned is a contract violation.
ALLOWED_DISTRIBUTION_OWNED = {
    "distribution.yaml",
    "profile.yaml",
    "SOUL.md",
    "config.yaml",
    "templates",
    "skills/marketing-core",
}

REQUIRED_SKILL_SECTIONS = [
    "## When to use",
    "## When not to use",
    "## Inputs",
    "## Evidence and sources",
    "## Procedure",
    "## Output contract",
    "## Verification",
    "## Approval boundaries",
    "## Blocked and failure behavior",
    "## Example",
    "## Related",
]

# Built dynamically so this file never triggers its own scan.
_TODO_WORDS = ["TO" + "DO", "FIX" + "ME", "TB" + "D", "XX" + "X"]
PLACEHOLDER_PATTERNS = [
    re.compile(r"<GITHUB_OWNER>"),
    re.compile(r"<REPOSITORY_NAME>"),
    re.compile(r"REPLACE" + r"_ME"),
    re.compile(r"CHANGE" + r"ME"),
    re.compile(r"lorem ipsum", re.IGNORECASE),
    re.compile(r"<<[A-Z_]+>>"),
]

SECRET_PATTERNS = [
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("OpenAI-style key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("Anthropic key", re.compile(r"\bsk-ant-[A-Za-z0-9_-]{10,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("Private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("Hardcoded credential", re.compile(
        r"(?i)\b(api[_-]?key|secret|password|token)\b\s*[:=]\s*['\"][A-Za-z0-9_\-/+=]{16,}['\"]"
    )),
]

PII_PATTERNS = [
    ("SSN-like number", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("Credit-card-like number", re.compile(r"\b(?:\d[ -]?){15}\d\b")),
]

RUNTIME_STATE_GLOBS = [
    "**/*.db", "**/*.sqlite", "**/*.sqlite3", "**/*.log",
    "**/.env", "**/.env.*", "**/auth.json", "**/__pycache__",
    "**/node_modules", "**/memories", "**/sessions", "**/local",
]

TEXT_EXTENSIONS = {".md", ".yaml", ".yml", ".json", ".py", ".sh", ".txt", ".gitignore"}

SKIP_DIRS = {".git"}


class Findings:
    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, check: str, message: str) -> None:
        self.items.append(f"[{check}] {message}")


def repo_files() -> list[Path]:
    out = []
    for path in sorted(REPO.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        out.append(path)
    return out


def text_files(files: list[Path]) -> list[Path]:
    return [
        p for p in files
        if p.is_file() and (p.suffix in TEXT_EXTENSIONS or p.name in {".gitignore", "LICENSE"})
    ]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def relpath(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


# ---------------------------------------------------------------- checks


def check_required_files(f: Findings) -> None:
    for rel in REQUIRED_FILES:
        if not (REPO / rel).is_file():
            f.add("required-files", f"missing: {rel}")


def check_yaml_json_validity(f: Findings, files: list[Path]) -> None:
    for path in files:
        if not path.is_file():
            continue
        rel = relpath(path)
        if path.suffix in {".yaml", ".yml"}:
            try:
                list(yaml.safe_load_all(read(path)))
            except yaml.YAMLError as exc:
                f.add("yaml", f"{rel}: {exc}")
        elif path.suffix == ".json":
            import json
            try:
                json.loads(read(path))
            except json.JSONDecodeError as exc:
                f.add("json", f"{rel}: {exc}")


def parse_frontmatter(path: Path) -> tuple[dict | None, str]:
    raw = path.read_bytes()
    if not raw.startswith(b"---\n"):
        return None, "frontmatter must start at byte zero with `---`"
    text = raw.decode("utf-8", errors="replace")
    end = text.find("\n---", 4)
    if end == -1:
        return None, "unterminated frontmatter block"
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        return None, f"invalid frontmatter YAML: {exc}"
    if not isinstance(data, dict):
        return None, "frontmatter must be a YAML mapping"
    return data, ""


def check_skills(f: Findings) -> None:
    seen_names: dict[str, str] = {}
    skills_root = REPO / "skills" / "marketing-core"
    if not skills_root.is_dir():
        f.add("skills", "skills/marketing-core/ missing")
        return
    actual_dirs = {p.name for p in skills_root.iterdir() if p.is_dir()}
    for extra in sorted(actual_dirs - set(SKILLS)):
        f.add("skills", f"unexpected skill directory: skills/marketing-core/{extra}")
    for skill in SKILLS:
        skill_md = skills_root / skill / "SKILL.md"
        rel = relpath(skill_md) if skill_md.exists() else f"skills/marketing-core/{skill}/SKILL.md"
        if not skill_md.is_file():
            continue  # reported by required-files
        fm, err = parse_frontmatter(skill_md)
        if fm is None:
            f.add("frontmatter", f"{rel}: {err}")
            continue
        for key in FRONTMATTER_REQUIRED:
            if key not in fm or fm[key] in (None, "", []):
                f.add("frontmatter", f"{rel}: missing required field `{key}`")
        name = str(fm.get("name", ""))
        if name != skill:
            f.add("frontmatter", f"{rel}: name `{name}` != directory `{skill}`")
        if name != name.lower():
            f.add("frontmatter", f"{rel}: name must be lowercase")
        if len(name) > MAX_NAME_LENGTH:
            f.add("frontmatter", f"{rel}: name exceeds {MAX_NAME_LENGTH} chars")
        if len(str(fm.get("description", ""))) > MAX_DESCRIPTION_LENGTH:
            f.add("frontmatter", f"{rel}: description exceeds {MAX_DESCRIPTION_LENGTH} chars")
        if name in seen_names:
            f.add("frontmatter", f"{rel}: duplicate skill name `{name}` (also {seen_names[name]})")
        seen_names[name] = rel
        if str(fm.get("license", "")) != LICENSE_ID:
            f.add("license", f"{rel}: frontmatter license must be `{LICENSE_ID}`")
        hermes_meta = (fm.get("metadata") or {}).get("hermes") or {}
        if not isinstance(hermes_meta.get("tags"), list) or not hermes_meta.get("tags"):
            f.add("frontmatter", f"{rel}: metadata.hermes.tags must be a non-empty list")
        related = hermes_meta.get("related_skills")
        if not isinstance(related, list) or not related:
            f.add("frontmatter", f"{rel}: metadata.hermes.related_skills must be a non-empty list")
        else:
            for other in related:
                if other not in SKILLS:
                    f.add("internal-refs", f"{rel}: related skill `{other}` does not exist")
        for stray in ("tags", "related_skills"):
            if stray in fm:
                f.add("frontmatter", f"{rel}: `{stray}` must live under metadata.hermes, not top-level")
        body = read(skill_md)
        if len(body) > MAX_SKILL_CONTENT_CHARS:
            f.add("frontmatter", f"{rel}: file exceeds {MAX_SKILL_CONTENT_CHARS} chars")
        for section in REQUIRED_SKILL_SECTIONS:
            if section not in body:
                f.add("skill-sections", f"{rel}: missing section `{section}`")


def check_internal_references(f: Findings, files: list[Path]) -> None:
    link_re = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
    template_re = re.compile(r"`(templates/[a-z0-9./-]+\.(?:md|yaml|yml))`")
    for path in files:
        if path.suffix != ".md":
            continue
        rel = relpath(path)
        content = read(path)
        for match in link_re.finditer(content):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                f.add("internal-refs", f"{rel}: broken link → {target}")
        for match in template_re.finditer(content):
            ref = match.group(1)
            # Skill files resolve template refs against their own directory
            # (the Hermes skill_view contract); the four shared shapes are
            # cited as profile-root paths, and the repo root installs at the
            # profile root, so it is the fallback. Non-skill files resolve
            # against the repo root only.
            if rel.startswith("skills/"):
                if not (path.parent / ref).is_file() and not (REPO / ref).is_file():
                    f.add("templates", f"{rel}: references missing {ref}")
            elif not (REPO / ref).is_file():
                f.add("templates", f"{rel}: references missing {ref}")


def check_license_consistency(f: Findings) -> None:
    lic = REPO / "LICENSE"
    if lic.is_file():
        text = read(lic)
        if "MIT License" not in text:
            f.add("license", "LICENSE: full MIT text missing")
        if COPYRIGHT_LINE not in text:
            f.add("license", f"LICENSE: missing `{COPYRIGHT_LINE}`")
    dist = REPO / "distribution.yaml"
    if dist.is_file():
        try:
            data = yaml.safe_load(read(dist)) or {}
            if data.get("license") != LICENSE_ID:
                f.add("license", f"distribution.yaml: license must be `{LICENSE_ID}`")
        except yaml.YAMLError:
            pass  # reported by yaml check
    readme = REPO / "README.md"
    if readme.is_file() and LICENSE_ID not in read(readme):
        f.add("license", "README.md: license not stated")


def check_placeholders_and_todos(f: Findings, files: list[Path]) -> None:
    this_file = Path(__file__).resolve()
    for path in files:
        if path.resolve() == this_file:
            continue
        rel = relpath(path)
        content = read(path)
        for word in _TODO_WORDS:
            for i, line in enumerate(content.splitlines(), 1):
                if re.search(rf"\b{word}\b", line):
                    f.add("todo", f"{rel}:{i}: contains `{word}`")
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(content):
                f.add("placeholders", f"{rel}: unresolved placeholder `{pattern.pattern}`")


def check_empty_examples(f: Findings) -> None:
    for folder in ("examples", "evals"):
        root = REPO / folder
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*")):
            if "results" in path.parts:
                continue  # generated transcripts, gitignored
            if path.is_file() and path.stat().st_size < 80:
                f.add("empty-files", f"{relpath(path)}: file is empty or trivially small")


def scan_secrets(f: Findings, label: str, content: str, where: str) -> None:
    for name, pattern in SECRET_PATTERNS:
        if pattern.search(content):
            f.add(label, f"{where}: possible {name}")


def check_secrets_and_pii(f: Findings, files: list[Path]) -> None:
    this_file = Path(__file__).resolve()
    for path in files:
        if path.resolve() == this_file:
            continue
        rel = relpath(path)
        content = read(path)
        scan_secrets(f, "secrets", content, rel)
        for name, pattern in PII_PATTERNS:
            if pattern.search(content):
                f.add("pii", f"{rel}: possible {name}")


def check_history_secrets(f: Findings) -> None:
    proc = subprocess.run(
        ["git", "-C", str(REPO), "log", "-p", "--all"],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        f.add("history", f"git log failed: {proc.stderr.strip()[:200]}")
        return
    for name, pattern in SECRET_PATTERNS:
        match = pattern.search(proc.stdout)
        if match:
            f.add("history", f"git history: possible {name} (`{match.group(0)[:12]}…`)")


def check_runtime_state(f: Findings) -> None:
    for pattern in RUNTIME_STATE_GLOBS:
        for path in REPO.glob(pattern):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            f.add("runtime-state", f"{relpath(path)}: runtime/user state must not be committed")


def check_symlinks(f: Findings, files: list[Path]) -> None:
    for path in files:
        if path.is_symlink():
            f.add("symlinks", f"{relpath(path)}: symlink not allowed")


def check_distribution_owned(f: Findings) -> None:
    dist = REPO / "distribution.yaml"
    if not dist.is_file():
        return
    try:
        data = yaml.safe_load(read(dist)) or {}
    except yaml.YAMLError:
        return
    owned = data.get("distribution_owned")
    if not isinstance(owned, list) or not owned:
        f.add("distribution-owned", "distribution.yaml: distribution_owned must be an explicit non-empty list")
        return
    normalized = [str(entry).strip().strip("/") for entry in owned]
    for entry_s in normalized:
        if entry_s not in ALLOWED_DISTRIBUTION_OWNED:
            f.add("distribution-owned", f"distribution.yaml: `{entry_s}` outside the approved runtime allowlist")
        if not (REPO / entry_s).exists():
            f.add("distribution-owned", f"distribution.yaml: owned path missing from repo: {entry_s}")
    for required in ("SOUL.md", "profile.yaml", "config.yaml", "skills/marketing-core", "distribution.yaml"):
        if required not in normalized:
            f.add("distribution-owned", f"distribution.yaml: `{required}` must be distribution-owned")
    requires = str(data.get("hermes_requires", ""))
    if not requires:
        f.add("distribution-owned", "distribution.yaml: hermes_requires must be set (the distribution_owned contract needs Hermes >=0.20.5)")


def check_ci_pinning(f: Findings) -> None:
    workflows = REPO / ".github" / "workflows"
    if not workflows.is_dir():
        return
    uses_re = re.compile(r"^\s*(?:-\s+)?uses:\s*([^\s#]+)", re.MULTILINE)
    sha_re = re.compile(r"@[0-9a-f]{40}$")
    for path in sorted(workflows.glob("*.yml")) + sorted(workflows.glob("*.yaml")):
        rel = relpath(path)
        for match in uses_re.finditer(read(path)):
            ref = match.group(1)
            if ref.startswith("./"):
                continue
            if not sha_re.search(ref):
                f.add("ci-pinning", f"{rel}: `{ref}` must be pinned to a full commit SHA")


def check_readme(f: Findings) -> None:
    readme = REPO / "README.md"
    if not readme.is_file():
        return
    content = read(readme)
    for label, cmd in [
        ("install command", INSTALL_CMD),
        ("automation install command", INSTALL_CMD_YES),
        ("direct chat command", CHAT_CMD),
        ("update command", UPDATE_CMD),
        ("removal command", REMOVE_CMD),
        ("kanban assignment", KANBAN_CMD_FRAGMENT),
    ]:
        if cmd not in content:
            f.add("readme", f"README.md: missing exact {label}: `{cmd}`")
    if content.count(COMMUNITY_URL) != 1:
        f.add("readme", f"README.md: community URL must appear exactly once (found {content.count(COMMUNITY_URL)})")


def check_community_link_containment(f: Findings, files: list[Path]) -> None:
    """The community URL lives in README.md only. Installed runtime files
    (identity, config, skills, templates) may not even name the community —
    it must never reach the agent's instructions or deliverables."""
    runtime_prefixes = (
        "distribution.yaml", "profile.yaml", "SOUL.md", "config.yaml",
        "skills/", "templates/",
    )
    for path in files:
        rel = relpath(path)
        if rel == "README.md":
            continue
        content = read(path)
        if COMMUNITY_URL in content:
            f.add("community-link", f"{rel}: community URL may only appear in README.md")
        if rel.startswith(runtime_prefixes) and "Agentic AI Academy" in content:
            f.add("community-link", f"{rel}: community promotion must not reach installed runtime files")


# ---------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--history", action="store_true", help="also scan git history for secrets")
    args = parser.parse_args()

    findings = Findings()
    files = repo_files()
    texts = text_files(files)

    check_required_files(findings)
    check_yaml_json_validity(findings, files)
    check_skills(findings)
    check_internal_references(findings, texts)
    check_license_consistency(findings)
    check_placeholders_and_todos(findings, texts)
    check_empty_examples(findings)
    check_secrets_and_pii(findings, texts)
    check_runtime_state(findings)
    check_symlinks(findings, files)
    check_distribution_owned(findings)
    check_ci_pinning(findings)
    check_readme(findings)
    check_community_link_containment(findings, texts)
    if args.history:
        check_history_secrets(findings)

    if findings.items:
        print(f"Validation FAILED — {len(findings.items)} finding(s):\n")
        for item in findings.items:
            print(f"  {item}")
        return 1
    print("Validation passed: all checks clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
