#!/bin/zsh
# Manage the auto_commit_push.sh background process

REPO_ROOT="/Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026"
PID_FILE="${REPO_ROOT}/.auto_commit_push.pid"

usage() {
    echo "Usage: $0 {start|stop|restart|status}"
    echo ""
    echo "Commands:"
    echo "  start   - Start the auto-commit background process"
    echo "  stop    - Stop the auto-commit background process"
    echo "  restart - Restart the auto-commit background process"
    echo "  status  - Check if the process is running"
    exit 1
}

check_status() {
    if [[ -f "$PID_FILE" ]]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null 2>&1; then
            echo "✓ Auto-commit process is running (PID: $PID)"
            return 0
        else
            echo "✗ Auto-commit process is not running (stale PID file)"
            return 1
        fi
    else
        echo "✗ Auto-commit process is not running"
        return 1
    fi
}

start_process() {
    if check_status > /dev/null 2>&1; then
        echo "Auto-commit is already running"
        check_status
        return 0
    fi
    
    echo "Starting auto-commit process..."
    cd "$REPO_ROOT" || exit 1
    nohup ./auto_commit_push.sh > /dev/null 2>&1 &
    NEW_PID=$!
    echo "$NEW_PID" > "$PID_FILE"
    sleep 1
    check_status
}

stop_process() {
    if [[ -f "$PID_FILE" ]]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null 2>&1; then
            echo "Stopping auto-commit process (PID: $PID)..."
            kill "$PID" 2>/dev/null
            sleep 1
            if ps -p "$PID" > /dev/null 2>&1; then
                echo "Process didn't stop gracefully, forcing..."
                kill -9 "$PID" 2>/dev/null
            fi
            rm -f "$PID_FILE"
            echo "✓ Auto-commit process stopped"
        else
            echo "Process not running, cleaning up PID file"
            rm -f "$PID_FILE"
        fi
    else
        echo "No PID file found, process is not running"
    fi
}

case "$1" in
    start)
        start_process
        ;;
    stop)
        stop_process
        ;;
    restart)
        stop_process
        echo ""
        start_process
        ;;
    status)
        check_status
        ;;
    *)
        usage
        ;;
esac
