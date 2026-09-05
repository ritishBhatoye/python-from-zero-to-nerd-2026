"""Tests for Setup Exercise 01 — Verify Environment."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("01_verify_environment")
    verify_environment = solution.verify_environment
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestVerifyEnvironment:
    def test_returns_required_keys(self):
        result = verify_environment()
        assert "python_version" in result
        assert "version_ok" in result
        assert "platform" in result
        assert "message" in result

    def test_version_format(self):
        result = verify_environment()
        parts = result["python_version"].split(".")
        assert len(parts) >= 2

    def test_message_matches_version_ok(self):
        result = verify_environment()
        if result["version_ok"]:
            assert result["message"] == "Ready"
        else:
            assert "3.12" in result["message"]
