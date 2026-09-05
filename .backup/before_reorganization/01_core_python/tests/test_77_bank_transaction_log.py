"""Tests for Exercise 77 — Bank Transaction Log."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("77_bank_transaction_log")
    calculate_balance = solution.calculate_balance
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestBankTransactionLog:
    def test_basic_example(self):
        transactions = ["D 300", "D 300", "W 200", "D 100"]
        result = calculate_balance(transactions)
        assert result == 500  # 300 + 300 - 200 + 100

    def test_only_deposits(self):
        transactions = ["D 1000", "D 500", "D 300"]
        result = calculate_balance(transactions)
        assert result == 1800

    def test_only_withdrawals(self):
        transactions = ["W 100", "W 200", "W 50"]
        result = calculate_balance(transactions)
        assert result == -350

    def test_balance_to_zero(self):
        transactions = ["D 100", "W 100"]
        result = calculate_balance(transactions)
        assert result == 0

    def test_empty_transactions(self):
        result = calculate_balance([])
        assert result == 0

    def test_single_deposit(self):
        result = calculate_balance(["D 1000"])
        assert result == 1000

    def test_single_withdrawal(self):
        result = calculate_balance(["W 500"])
        assert result == -500

    def test_complex_sequence(self):
        transactions = ["D 1000", "W 500", "W 300", "D 200", "D 100"]
        result = calculate_balance(transactions)
        assert result == 500  # 1000 - 500 - 300 + 200 + 100
