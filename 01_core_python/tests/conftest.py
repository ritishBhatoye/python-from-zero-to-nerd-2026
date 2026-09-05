"""Shared pytest helpers for importing learner solutions."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def import_solution(module_name: str, phase_dir: Path | None = None) -> object:
    """Import a solution module from the phase solutions directory."""
    if phase_dir is None:
        phase_dir = Path(__file__).resolve().parent.parent

    solutions_dir = phase_dir / "solutions"
    module_path = solutions_dir / f"{module_name}.py"

    if not module_path.exists():
        raise ModuleNotFoundError(
            f"Solution not found: {module_path}\n"
            f"Create your implementation before running tests."
        )

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {module_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
