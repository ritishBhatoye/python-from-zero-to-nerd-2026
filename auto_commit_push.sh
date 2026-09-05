#!/bin/zsh
# Delegates to the gitignored background auto-push helper.
exec "$(dirname "$0")/.auto_commit_push.sh"
