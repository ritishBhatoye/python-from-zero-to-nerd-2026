"""Tests for Exercise 64 — Custom Exception."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("64_custom_exception")
    withdraw = solution.withdraw
    InsufficientFundsError = solution.InsufficientFundsError
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestCustomException:
    def test_successful_withdrawal(self):
        assert withdraw(100.0, 50.0) == 50.0
        assert withdraw(100.0, 100.0) == 0.0

    def test_invalid_amount(self):
        with pytest.raises(ValueError):
            withdraw(100.0, 0.0)
        with pytest.raises(ValueError):
            withdraw(100.0, -50.0)

    def test_insufficient_funds(self):
        with pytest.raises(InsufficientFundsError) as exc_info:
            withdraw(100.0, 150.0)
        
        assert exc_info.value.balance == 100.0
        assert exc_info.value.amount == 150.0
