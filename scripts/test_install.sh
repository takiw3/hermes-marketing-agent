#!/usr/bin/env bash
# Isolated installation tests for the marketing profile distribution.
#
# Runs every install/update check against throwaway HOME and HERMES_HOME
# directories — it never reads or writes your real Hermes profiles.
#
# Requirements: a Hermes CLI >= 0.20.0. Below that the path-aware
# distribution_owned allowlist does not exist, the installer copies every
# top-level repo entry, and these tests fail by design.
#
# Usage:
#   bash scripts/test_install.sh                          # from the local repo
#   HERMES_BIN=/path/to/hermes bash scripts/test_install.sh
#   SOURCE_URL=github.com/owner/repo bash scripts/test_install.sh   # from git
#
# Exit code 0 = all checks passed.

set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HERMES_BIN="${HERMES_BIN:-hermes}"
TESTROOT="$(mktemp -d "${TMPDIR:-/tmp}/hermes-mkt-test.XXXXXX")"

PASS=0
FAIL=0

say()  { printf '%s\n' "$*"; }
ok()   { PASS=$((PASS+1)); say "  pass  $*"; }
bad()  { FAIL=$((FAIL+1)); say "  FAIL  $*"; }
require() { # require <description> <command...>
  local desc="$1"; shift
  if "$@" >/dev/null 2>&1; then ok "$desc"; else bad "$desc"; fi
}

cleanup() { rm -rf "$TESTROOT"; }
trap cleanup EXIT

command -v "$HERMES_BIN" >/dev/null 2>&1 || {
  say "hermes CLI not found (HERMES_BIN=$HERMES_BIN). Install Hermes first."
  exit 2
}

# --- isolated environment -------------------------------------------------
# HERMES_HOME must be OUTSIDE ~/.hermes (a subdir of ~/.hermes resolves the
# profiles root back to the real one). HOME is also redirected so the
# --alias wrapper lands in the sandbox, not in the real ~/.local/bin.
export HOME="$TESTROOT/home"
export HERMES_HOME="$TESTROOT/hermes-root"
mkdir -p "$HOME/.local/bin" "$HERMES_HOME"
PROFILE_DIR="$HERMES_HOME/profiles/marketing"

VERSION_LINE="$("$HERMES_BIN" --version 2>/dev/null | head -1)"
say "Hermes under test: ${VERSION_LINE:-unknown}"
say "Sandbox: $TESTROOT"
say ""

# --- stage the source -----------------------------------------------------
# Install from a pristine copy of the repo so the update test can mutate the
# source without touching the working tree.
if [ -n "${SOURCE_URL:-}" ]; then
  SOURCE="$SOURCE_URL"
else
  SOURCE="$TESTROOT/repo-v1"
  mkdir -p "$SOURCE"
  (cd "$REPO" && tar -cf - --exclude .git --exclude evals/results .) | (cd "$SOURCE" && tar -xf -)
fi

say "== install =="
if "$HERMES_BIN" profile install "$SOURCE" --alias -y > "$TESTROOT/install.log" 2>&1; then
  ok "manifest accepted and install succeeded (hermes profile install ... --alias -y)"
else
  bad "install failed — $TESTROOT/install.log:"
  sed 's/^/        /' "$TESTROOT/install.log"
  exit 1
fi

require "profile directory created" test -d "$PROFILE_DIR"

say ""
say "== profile info / show / describe =="
INFO="$("$HERMES_BIN" profile info marketing 2>&1)"
require "info reports the distribution name"    grep -q "marketing" <<<"$INFO"
VERSION="$(sed -n 's/^version: *//p' "$REPO/distribution.yaml" | head -1)"
require "info reports version $VERSION"         grep -q "$VERSION" <<<"$INFO"
require "info reports the source"               grep -q "$SOURCE" <<<"$INFO"
require "info reports hermes_requires >=0.20.0" grep -q ">=0.20.0" <<<"$INFO"

SHOW="$("$HERMES_BIN" profile show marketing 2>&1)"
require "show finds the profile"                grep -q "marketing" <<<"$SHOW"
require "show reports 17 skills"                grep -Eq "Skills:? *17" <<<"$SHOW"
require "identity (SOUL.md) installed"          test -f "$PROFILE_DIR/SOUL.md"

DESCRIBE="$("$HERMES_BIN" profile describe marketing 2>&1)"
require "routing description present"           grep -q "Owns marketing research" <<<"$DESCRIBE"
require "routing description states approval rule" grep -q "without approval" <<<"$DESCRIBE"

say ""
say "== installed payload =="
for skill in \
  marketing-intake-and-routing marketing-strategy brand-voice-analysis \
  customer-and-offer-research conversion-copywriting email-sequences \
  social-content-calendar social-performance-analysis social-carousel-creation \
  social-script-creation paid-ad-campaigns funnel-analysis \
  competitor-intelligence website-cro-analysis measurement-and-experimentation \
  marketing-reporting weekly-marketing-review; do
  require "skill installed: $skill" test -f "$PROFILE_DIR/skills/marketing-core/$skill/SKILL.md"
done

require "shared templates installed" test -f "$PROFILE_DIR/templates/handoff-result.md"
require "config.yaml installed"      test -f "$PROFILE_DIR/config.yaml"
require "profile.yaml installed"     test -f "$PROFILE_DIR/profile.yaml"

for banned in README.md LICENSE CHANGELOG.md CONTRIBUTING.md SECURITY.md \
              .gitignore docs evals examples scripts .github; do
  if [ -e "$PROFILE_DIR/$banned" ]; then
    bad "repository file leaked into profile: $banned"
  else
    ok "not installed (correct): $banned"
  fi
done

if find "$PROFILE_DIR" -type l | grep -q .; then
  bad "symlinks found in installed profile"
else
  ok "no symlinks in installed profile"
fi

say ""
say "== alias =="
WRAPPER="$HOME/.local/bin/marketing"
require "alias wrapper created"        test -x "$WRAPPER"
require "wrapper targets the profile"  grep -q '\-p "\?marketing"\?\|--profile "\?marketing"\?\|-p marketing' "$WRAPPER"

say ""
say "== README command parity =="
README_CMD="hermes profile install https://github.com/takiw3/hermes-marketing-agent --alias"
if grep -qF "$README_CMD" "$REPO/README.md"; then
  ok "README primary install command matches the tested command form"
else
  bad "README primary install command missing or different"
fi

say ""
say "== update preservation =="
if [ -n "${SOURCE_URL:-}" ]; then
  say "  skip  update preservation runs only for local-source tests"
else
  # Plant user-owned data the update must never touch.
  echo "EXAMPLE_MARKER=user-owned" > "$PROFILE_DIR/.env"
  mkdir -p "$PROFILE_DIR/memories" "$PROFILE_DIR/sessions" "$PROFILE_DIR/local"
  echo "user memory marker" > "$PROFILE_DIR/memories/probe.md"
  echo "user session marker" > "$PROFILE_DIR/sessions/probe.json"
  echo "business profile marker" > "$PROFILE_DIR/local/business-profile.md"
  printf '\n# user-config-override-marker\n' >> "$PROFILE_DIR/config.yaml"
  mkdir -p "$PROFILE_DIR/skills/custom-user-skill"
  printf -- '---\nname: custom-user-skill\ndescription: User-created probe skill.\n---\nBody.\n' \
    > "$PROFILE_DIR/skills/custom-user-skill/SKILL.md"

  # Mutate the staged source into a bumped version.
  NEWVER="${VERSION%.*}.$(( ${VERSION##*.} + 1 ))"
  sed -i.bak "s/^version: .*/version: $NEWVER/" "$SOURCE/distribution.yaml" && rm -f "$SOURCE/distribution.yaml.bak"
  printf '\n<!-- update-marker-v101 -->\n' >> "$SOURCE/SOUL.md"

  if "$HERMES_BIN" profile update marketing -y > "$TESTROOT/update.log" 2>&1; then
    ok "profile update succeeded"
  else
    bad "profile update failed — $TESTROOT/update.log:"
    sed 's/^/        /' "$TESTROOT/update.log"
  fi

  require ".env preserved"                    grep -q "EXAMPLE_MARKER=user-owned" "$PROFILE_DIR/.env"
  require "memories preserved"                test -f "$PROFILE_DIR/memories/probe.md"
  require "sessions preserved"                test -f "$PROFILE_DIR/sessions/probe.json"
  require "local/ preserved"                  test -f "$PROFILE_DIR/local/business-profile.md"
  require "config.yaml override preserved"    grep -q "user-config-override-marker" "$PROFILE_DIR/config.yaml"
  require "user-created skill preserved"      test -f "$PROFILE_DIR/skills/custom-user-skill/SKILL.md"
  require "distribution-owned SOUL.md updated" grep -q "update-marker-v101" "$PROFILE_DIR/SOUL.md"
  require "manifest version updated to $NEWVER"  grep -q "$NEWVER" <<<"$("$HERMES_BIN" profile info marketing 2>&1)"
fi

say ""
say "== result: $PASS passed, $FAIL failed =="
[ "$FAIL" -eq 0 ]
