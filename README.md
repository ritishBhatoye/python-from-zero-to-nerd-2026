# Python: From Zero to Nerd (2026)

A structured, practical Python learning repository — from fundamentals through advanced engineering to expert-level internals.

## Who This Is For

This repository is built by a learner (B.Tech CSE, AI & ML background) who has completed Python fundamentals and is progressing toward production-quality Python engineering. It is **not** a collection of copied tutorials. Every implementation here was written, reviewed, and refined through a deliberate learning process.

If you are at a similar stage — comfortable with basic syntax but wanting to build real understanding — this repository may be useful to you.

## Learning Philosophy

### Practical-First

Every concept is learned through implementation, not passive reading.

The cycle for each topic:

```
CONCEPT → PRACTICAL PROBLEM → MY IMPLEMENTATION → TESTING → REVIEW → IMPROVEMENT → DOCUMENTATION → COMMIT
```

### No Copy-Paste Learning

Problems are given with requirements and constraints, not solutions. Implementation comes first; reference solutions appear only after a working attempt.

### Progressive Difficulty

Each major topic progresses through levels:

| Level | Focus |
|-------|-------|
| **Foundation** | Core implementation |
| **Practical** | Real-world scenario |
| **Advanced** | Multiple concepts combined |
| **Engineering** | Production-quality considerations |
| **Nerd Mode** | Internals, CPython, bytecode, performance |

Not every topic warrants all five levels — trivial topics stay practical.

## Repository Roadmap

| Phase | Directory | Focus |
|-------|-----------|-------|
| 0 | `00_setup/` | Environment, tooling, Git workflow |
| 1 | `01_core_python/` | Variables, data types, loops, functions, exceptions |
| 2 | `02_intermediate_python/` | Generators, decorators, closures, iterators, type hints |
| 3 | `03_oop/` | Classes, inheritance, composition, design |
| 4 | `04_standard_library/` | pathlib, collections, itertools, json, logging, etc. |
| 5 | `05_testing_quality/` | pytest, mocking, coverage, linting, formatting |
| 6 | `06_advanced_python/` | Metaclasses, descriptors, advanced typing, protocols |
| 7 | `07_concurrency_async/` | threading, multiprocessing, asyncio, GIL |
| 8 | `08_networking_apis/` | HTTP, REST, FastAPI, Pydantic, WebSockets |
| 9 | `09_databases/` | SQLite, SQLAlchemy, transactions, repository pattern |
| 10 | `10_internals_performance/` | CPython, bytecode, profiling, memory, optimization |
| 11 | `11_algorithms_data_structures/` | Implementations from scratch, complexity analysis |
| 12 | `12_design_patterns/` | Factory, Strategy, Observer, DI, system design |
| 13 | `13_automation/` | File processing, CLI tools, scraping, scheduling |
| 14 | `14_data_engineering/` | NumPy, Pandas, ETL pipelines, data validation |
| 15 | `15_ai_ml_python/` | scikit-learn, PyTorch, from-scratch implementations |

The `projects/` directory contains standalone projects organized by difficulty level.

## How Challenges Work

Each topic includes:

- **Problem statement** with clear requirements and constraints
- **Test cases** with expected behavior
- **Hints** (progressive — no immediate solutions)
- **Bonus challenges** for deeper exploration

The implementation is written first, then reviewed for correctness, edge cases, Pythonic style, and engineering quality.

## How to Run the Code

### Prerequisites

- Python 3.12+
- A virtual environment (recommended)

### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/python-from-zero-to-nerd-2026.git
cd python-from-zero-to-nerd-2026

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux

# Install development tools
pip install pytest ruff mypy
```

### Running a specific file

```bash
python 01_core_python/06_data_structures/word_frequency.py
```

### Running tests

```bash
pytest                          # Run all tests
pytest 01_core_python/          # Run tests for a specific phase
pytest -v                       # Verbose output
```

## Testing Philosophy

Code that isn't tested is code that might not work.

Every non-trivial implementation includes tests. The goal is not 100% coverage for its own sake — it's the ability to answer:

> "How do I prove this code works?"

Tests are introduced formally in Phase 5, but basic test cases accompany implementations from the start.

## Git Workflow

Commits follow conventional style and represent meaningful progress:

```
feat: implement generator-based log processor
docs: document Python decorators with examples
test: add edge case coverage for word frequency analyzer
refactor: extract validation logic into separate function
```

Quality over quantity. No artificial commit inflation.

## Progress Tracking

| Phase | Status |
|-------|--------|
| Phase 0 — Setup | 🟡 In progress |
| Phase 1 — Core Python | 🔴 Not started |
| Phase 2 — Intermediate Python | 🔴 Not started |
| Phase 3 — OOP | 🔴 Not started |
| Phase 4 — Standard Library | 🔴 Not started |
| Phase 5 — Testing & Quality | 🔴 Not started |
| Phase 6 — Advanced Python | 🔴 Not started |
| Phase 7 — Concurrency & Async | 🔴 Not started |
| Phase 8 — Networking & APIs | 🔴 Not started |
| Phase 9 — Databases | 🔴 Not started |
| Phase 10 — Internals & Performance | 🔴 Not started |
| Phase 11 — Algorithms & DS | 🔴 Not started |
| Phase 12 — Design Patterns | 🔴 Not started |
| Phase 13 — Automation | 🔴 Not started |
| Phase 14 — Data Engineering | 🔴 Not started |
| Phase 15 — AI/ML Python | 🔴 Not started |

## License

[MIT](LICENSE)
