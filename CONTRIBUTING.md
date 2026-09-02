# Contributing & Learning Workflow

This repository follows a deliberate learning workflow. Every piece of code
represents genuine understanding, not copied solutions.

## Workflow for Each Challenge

```
1. Read the problem statement and constraints
2. Plan your approach (pseudocode or notes)
3. Implement the solution from scratch
4. Write tests to verify correctness
5. Run tests and fix failures
6. Review for edge cases and Pythonic style
7. Document what you learned
8. Commit with a meaningful message
```

## Commit Convention

Commits use [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Use |
|--------|-----|
| `feat:` | New implementation or feature |
| `fix:` | Bug fix in existing code |
| `test:` | Adding or improving tests |
| `docs:` | Documentation changes |
| `refactor:` | Code restructuring without behavior change |
| `chore:` | Tooling, config, or maintenance |

## Code Quality Checklist

Before committing, verify:

- [ ] Code runs without errors
- [ ] Tests pass (`pytest`)
- [ ] No lint warnings (`ruff check`)
- [ ] Type hints are present where appropriate
- [ ] Docstrings explain *why*, not just *what*

## Branch Strategy

- `main` — stable, reviewed implementations
- Feature branches for larger multi-file work

## Directory Conventions

- Each phase directory (`01_core_python/`, etc.) contains topic subdirectories
- Each topic subdirectory contains the implementation, tests, and a brief README
- Filenames use `snake_case`
- Test files are prefixed with `test_`
