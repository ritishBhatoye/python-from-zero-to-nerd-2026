#!/bin/zsh
# Create a meaningful conventional commit after completing an exercise.
#
# Usage:
#   ./scripts/commit_exercise.sh feat core 01_personal_expense_calculator
#   ./scripts/commit_exercise.sh test setup 02_hello_pytest
#
# Types: feat, test, refactor, docs, fix

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

if [[ $# -lt 3 ]]; then
  echo "Usage: $0 <type> <scope> <exercise_slug>" >&2
  echo "Example: $0 feat core 01_personal_expense_calculator" >&2
  exit 1
fi

commit_type="$1"
scope="$2"
slug="$3"
message="${commit_type}(${scope}): solve ${slug//_/ }"

if [[ -z "$(git status --porcelain)" ]]; then
  echo "No changes to commit." >&2
  exit 1
fi

git add -A
git commit -m "$message"
echo "Committed: $message"
