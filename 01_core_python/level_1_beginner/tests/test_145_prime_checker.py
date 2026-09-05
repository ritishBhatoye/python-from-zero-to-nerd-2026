"""Tests for Exercise 51 — Prime Checker."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("51_prime_checker")
    is_prime = solution.is_prime
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestPrimeChecker:
    def test_primes(self):
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True
        assert is_prime(97) is True

    def test_non_primes(self):
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False
        assert is_prime(100) is False

    def test_edge_cases(self):
        assert is_prime(1) is False
        assert is_prime(0) is False
        assert is_prime(-1) is False
        assert is_prime(-5) is False
