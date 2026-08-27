#!/usr/bin/env python3
"""Behavior evaluation runner for the marketing profile distribution.

Default mode validates every fixture in evals/ (schema, unique ids, suite
completeness) — this is what CI runs, and it needs no Hermes runtime.

--live executes each scenario against a real installed profile. That requires:

  1. The `hermes` CLI on PATH.
  2. HERMES_EVAL_HOME — an isolated HERMES_HOME directory where the
     `marketing` profile is installed AND model credentials are configured.
     Never point this at your real Hermes home; live runs write sessions and
     memory into whatever home they are given.
  3. HERMES_EVAL_CONFIRM=yes — an explicit acknowledgment that live runs
     spend model-provider credits.

If any prerequisite is missing, every eval is reported as `not run` with the
exact missing prerequisite. An unrun eval is never reported as passed.

Live runs capture full transcripts to evals/results/<id>.transcript.md and
report `ran (judgment pending)` — pass/fail is decided against the fixture's
must/must_not lists by a reviewer (or a judge model), not assumed by this
script.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML is required: python3 -m pip install pyyaml", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).resolve().parent.parent
EVALS_DIR = REPO / "evals"
RESULTS_DIR = EVALS_DIR / "results"
EXPECTED_COUNT = 18
REQUIRED_KEYS = ("id", "title", "setup", "input", "must", "must_not", "pass_criteria")
LIST_KEYS = ("must", "must_not")
PROFILE = "marketing"
LIVE_TIMEOUT_SECONDS = 600


def load_fixtures() -> tuple[list[dict], list[str]]:
    """Load every eval fixture; return (fixtures, errors)."""
    errors: list[str] = []
    fixtures: list[dict] = []
    files = sorted(p for p in EVALS_DIR.glob("*.yaml"))
    if len(files) != EXPECTED_COUNT:
        errors.append(
            f"expected {EXPECTED_COUNT} eval fixtures in evals/, found {len(files)}"
        )
    seen_ids: set[str] = set()
    for path in files:
        rel = path.relative_to(REPO)
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: invalid YAML: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{rel}: fixture must be a YAML mapping")
            continue
        for key in REQUIRED_KEYS:
            if key not in data or data[key] in (None, "", []):
                errors.append(f"{rel}: missing or empty required key `{key}`")
        for key in LIST_KEYS:
            if key in data and not isinstance(data[key], list):
                errors.append(f"{rel}: `{key}` must be a list")
        eval_id = data.get("id")
        if isinstance(eval_id, str):
            if eval_id in seen_ids:
                errors.append(f"{rel}: duplicate eval id `{eval_id}`")
            seen_ids.add(eval_id)
            if not path.stem.startswith(eval_id.split("-")[0]):
                # ids are prefixed with the same number as the filename
                pass
        data["_path"] = rel.as_posix()
        fixtures.append(data)
    return fixtures, errors


def live_prerequisites() -> list[str]:
    """Return the list of missing prerequisites for a live run."""
    missing: list[str] = []
    if shutil.which("hermes") is None:
        missing.append("`hermes` CLI not found on PATH")
    eval_home = os.environ.get("HERMES_EVAL_HOME", "")
    if not eval_home:
        missing.append(
            "HERMES_EVAL_HOME not set (isolated HERMES_HOME with the "
            "marketing profile installed and model credentials configured)"
        )
    elif not Path(eval_home).is_dir():
        missing.append(f"HERMES_EVAL_HOME does not exist: {eval_home}")
    if os.environ.get("HERMES_EVAL_CONFIRM", "") != "yes":
        missing.append(
            "HERMES_EVAL_CONFIRM=yes not set (explicit acknowledgment that "
            "live runs spend model-provider credits)"
        )
    return missing


def compose_prompt(fixture: dict) -> str:
    """Build the one-shot prompt for a scenario."""
    return (
        "You are being evaluated on a synthetic scenario. Everything below "
        "is fictional test data.\n\n"
        f"=== SCENARIO STATE ===\n{fixture['setup']}\n\n"
        f"=== INCOMING TASK ===\n{fixture['input']}\n\n"
        "Respond exactly as you would to this task in production."
    )


def run_live(fixtures: list[dict]) -> int:
    missing = live_prerequisites()
    if missing:
        print("Live run prerequisites missing — no eval was executed:\n")
        for item in missing:
            print(f"  - {item}")
        print()
        for fixture in fixtures:
            print(f"  not run   {fixture['id']}  (missing prerequisites above)")
        print(
            "\nResult: all evals `not run`. An unrun eval is never reported "
            "as passed."
        )
        return 0

    RESULTS_DIR.mkdir(exist_ok=True)
    env = dict(os.environ)
    env["HERMES_HOME"] = os.environ["HERMES_EVAL_HOME"]
    exit_code = 0
    for fixture in fixtures:
        eval_id = fixture["id"]
        transcript = RESULTS_DIR / f"{eval_id}.transcript.md"
        cmd = ["hermes", "-z", compose_prompt(fixture)]
        try:
            proc = subprocess.run(
                cmd,
                env=env,
                capture_output=True,
                text=True,
                timeout=LIVE_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            print(f"  error     {eval_id}  (timed out after {LIVE_TIMEOUT_SECONDS}s)")
            exit_code = 1
            continue
        body = [
            f"# Transcript — {eval_id}",
            "",
            f"Fixture: `{fixture['_path']}`",
            "",
            "## Agent response",
            "",
            proc.stdout.strip() or "(empty response)",
        ]
        if proc.returncode != 0:
            body += ["", "## Runner stderr", "", proc.stderr.strip()]
        transcript.write_text("\n".join(body) + "\n", encoding="utf-8")
        status = "ran" if proc.returncode == 0 else "error"
        if status == "error":
            exit_code = 1
        print(f"  {status:<9} {eval_id}  → {transcript.relative_to(REPO)}")
    print(
        "\nTranscripts captured. Judge each against its fixture's must/"
        "must_not lists before reporting pass/fail — `ran` is not `passed`."
    )
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--live",
        action="store_true",
        help="execute scenarios against an installed profile (see module docstring)",
    )
    args = parser.parse_args()

    fixtures, errors = load_fixtures()
    if errors:
        print("Fixture validation FAILED:\n")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(f"Fixture validation passed: {len(fixtures)} evals.\n")
    if not args.live:
        for fixture in fixtures:
            print(f"  {fixture['id']:<32} {fixture['title']}")
        print("\nRun with --live to execute (see prerequisites in --help).")
        return 0

    return run_live(fixtures)


if __name__ == "__main__":
    sys.exit(main())
