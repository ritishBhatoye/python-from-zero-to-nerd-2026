"""Tests for Setup Exercise 04 — Commit Message Builder."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("04_commit_message_builder")
    build_commit_message = solution.build_commit_message
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestBuildCommitMessage:
    def test_feat_core(self):
        msg = build_commit_message("feat", "core", "01_personal_expense_calculator")
        assert msg == "feat(core): solve 01 personal expense calculator"

    def test_invalid_type_raises(self):
        with pytest.raises(ValueError):
            build_commit_message("wip", "core", "test")

    def test_empty_scope_raises(self):
        with pytest.raises(ValueError):
            build_commit_message("feat", "", "test")
