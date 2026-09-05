#!/bin/zsh
# Ensures auto_commit_push.sh is running, but doesn't start duplicates

REPO_ROOT="/Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026"
SCRIPT_NAME="auto_commit_push.sh"
PID_FILE="${REPO_ROOT}/.auto_commit_push.pid"

cd "$REPO_ROOT" || exit 1

# Check if already running
if [[ -f "$PID_FILE" ]]; then
    OLD_PID=$(cat "$PID_FILE")
    if ps -p "$OLD_PID" > /dev/null 2>&1; then
        # Already running, exit silently
        exit 0
    else
        # Stale PID file, remove it
        rm -f "$PID_FILE"
    fi
fi

# Start the auto-commit script in background
nohup "./${SCRIPT_NAME}" > /dev/null 2>&1 &
NEW_PID=$!

# Save the PID
echo "$NEW_PID" > "$PID_FILE"

exit 0
