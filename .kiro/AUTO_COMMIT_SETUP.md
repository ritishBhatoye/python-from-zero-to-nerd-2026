# Auto Commit & Push Setup

This repository is configured to automatically commit and push changes to Git whenever you work on files.

## How It Works

1. **Background Process**: `auto_commit_push.sh` runs continuously in the background
2. **Automatic Triggers**: Kiro hooks ensure the process starts when:
   - You start a new Kiro session (`SessionStart` hook)
   - You save any file in the repository (`PostFileSave` hook)
3. **Smart Commits**: The script generates human-like commit messages based on changed files
4. **Cooldown**: Only pushes every 120 seconds (2 minutes) to avoid spam

## Managing the Auto-Commit Process

Use the management script:

```bash
# Check if it's running
.kiro/scripts/manage_auto_commit.sh status

# Start the process
.kiro/scripts/manage_auto_commit.sh start

# Stop the process
.kiro/scripts/manage_auto_commit.sh stop

# Restart the process
.kiro/scripts/manage_auto_commit.sh restart
```

## Configuration

The auto-commit behavior is controlled by:

- **Main script**: `auto_commit_push.sh` (delegates to `.auto_commit_push.sh`)
- **Cooldown**: 120 seconds between pushes (configurable in `.auto_commit_push.sh`)
- **Hooks**: 
  - `.kiro/hooks/auto-commit-on-session-start.json`
  - `.kiro/hooks/auto-commit-on-file-activity.json`

## What Gets Committed

- All staged changes
- All unstaged changes
- All untracked files

The script runs `git add .` before committing, so everything in your working directory will be included (except gitignored files).

## Commit Message Examples

The script generates varied commit messages like:
- `refactor: 01_core_python/solutions/71_string_list_tuple_converter.py`
- `update: README.md`
- `fix: 01_core_python/tests/test_85_docstring_explorer.py`

## Troubleshooting

**Process not running:**
```bash
.kiro/scripts/manage_auto_commit.sh start
```

**Too many commits:**
- Increase `COOLDOWN_SECONDS` in `.auto_commit_push.sh`

**Want to disable temporarily:**
```bash
.kiro/scripts/manage_auto_commit.sh stop
```

**Check recent activity:**
```bash
git log --oneline -10
```

## Files

- `auto_commit_push.sh` - Main entry point
- `.auto_commit_push.sh` - Actual implementation (gitignored)
- `.last_push_time` - Tracks last push timestamp
- `.auto_commit_push.pid` - Process ID file
- `.kiro/hooks/auto-commit-on-session-start.json` - SessionStart hook
- `.kiro/hooks/auto-commit-on-file-activity.json` - PostFileSave hook
- `.kiro/scripts/ensure_auto_commit_running.sh` - Ensures single instance
- `.kiro/scripts/manage_auto_commit.sh` - Management utility
