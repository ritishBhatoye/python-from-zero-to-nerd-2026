"""
Tests for Diagnostic Challenge #1 — Transaction Log Analyzer

Run with:
    cd /Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026
    python -m pytest 00_setup/diagnostics/tests/test_transaction_log_analyzer.py -v
"""

import sys
import os

# Add the solutions directory to the path so we can import the module
sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "solutions"),
)

from transaction_log_analyzer import analyze_transaction_logs


# ---------------------------------------------------------------------------
# Test 1: Main sample input from the problem statement
# ---------------------------------------------------------------------------
class TestMainSample:
    RAW_LOGS = [
        "2026-09-01T08:00:00 | user_alice | DEPOSIT | 1200.50",
        "2026-09-01T08:05:00 | user_bob | WITHDRAWAL | 150.00",
        "invalid | log | entry",
        "2026-09-01T08:10:00 | user_alice | TRANSFER | 500.00",
        "2026-09-01T08:15:00 | user_charlie | DEPOSIT | -50.00",
        "2026-09-01T08:20:00 | user_bob | REFUND | 100.00",
        "2026-09-01T08:25:00 | user_alice | WITHDRAWAL | abc",
        "  2026-09-01T08:30:00  |  user_david  |  DEPOSIT  |  750.25  ",
    ]

    def setup_method(self):
        self.result = analyze_transaction_logs(self.RAW_LOGS)

    def test_total_records(self):
        assert self.result["total_records"] == 8

    def test_valid_records(self):
        assert self.result["valid_records"] == 4

    def test_corrupted_records(self):
        assert self.result["corrupted_records"] == 4

    def test_total_volume(self):
        assert self.result["total_volume"] == 2600.75

    def test_breakdown_deposit(self):
        dep = self.result["breakdown_by_type"]["DEPOSIT"]
        assert dep["count"] == 2
        assert dep["total"] == 1950.75

    def test_breakdown_withdrawal(self):
        wd = self.result["breakdown_by_type"]["WITHDRAWAL"]
        assert wd["count"] == 1
        assert wd["total"] == 150.0

    def test_breakdown_transfer(self):
        tr = self.result["breakdown_by_type"]["TRANSFER"]
        assert tr["count"] == 1
        assert tr["total"] == 500.0

    def test_high_value_transactions(self):
        hvt = self.result["high_value_transactions"]
        assert len(hvt) == 3
        # Must be sorted by amount descending
        assert hvt[0] == {"user_id": "user_alice", "type": "DEPOSIT", "amount": 1200.50}
        assert hvt[1] == {"user_id": "user_david", "type": "DEPOSIT", "amount": 750.25}
        assert hvt[2] == {"user_id": "user_alice", "type": "TRANSFER", "amount": 500.0}

    def test_unique_users(self):
        assert self.result["unique_users"] == ["user_alice", "user_bob", "user_david"]


# ---------------------------------------------------------------------------
# Test 2: Empty input
# ---------------------------------------------------------------------------
class TestEmptyInput:
    def test_empty_list(self):
        result = analyze_transaction_logs([])
        assert result["total_records"] == 0
        assert result["valid_records"] == 0
        assert result["corrupted_records"] == 0
        assert result["total_volume"] == 0.0
        assert result["high_value_transactions"] == []
        assert result["unique_users"] == []
        for txn_type in ("DEPOSIT", "WITHDRAWAL", "TRANSFER"):
            assert result["breakdown_by_type"][txn_type]["count"] == 0
            assert result["breakdown_by_type"][txn_type]["total"] == 0.0


# ---------------------------------------------------------------------------
# Test 3: All corrupted
# ---------------------------------------------------------------------------
class TestAllCorrupted:
    def test_no_valid_records(self):
        logs = [
            "",
            "only one field",
            "a | b",
            "a | b | DEPOSIT | -10",
            "a | b | INVALID | 100",
            "a | b | DEPOSIT | 0",
            "a | b | DEPOSIT | not_a_number",
            "a |  | DEPOSIT | 100",
        ]
        result = analyze_transaction_logs(logs)
        assert result["total_records"] == len(logs)
        assert result["valid_records"] == 0
        assert result["corrupted_records"] == len(logs)
        assert result["total_volume"] == 0.0


# ---------------------------------------------------------------------------
# Test 4: All valid
# ---------------------------------------------------------------------------
class TestAllValid:
    def test_every_record_valid(self):
        logs = [
            "ts1 | user_a | DEPOSIT | 100.00",
            "ts2 | user_b | WITHDRAWAL | 200.00",
            "ts3 | user_c | TRANSFER | 300.00",
        ]
        result = analyze_transaction_logs(logs)
        assert result["total_records"] == 3
        assert result["valid_records"] == 3
        assert result["corrupted_records"] == 0
        assert result["total_volume"] == 600.0


# ---------------------------------------------------------------------------
# Test 5: High value boundary — exactly 500.0 should be included
# ---------------------------------------------------------------------------
class TestHighValueBoundary:
    def test_exactly_500_included(self):
        logs = [
            "ts | user_x | DEPOSIT | 500.00",
            "ts | user_y | DEPOSIT | 499.99",
        ]
        result = analyze_transaction_logs(logs)
        hvt = result["high_value_transactions"]
        assert len(hvt) == 1
        assert hvt[0]["amount"] == 500.0


# ---------------------------------------------------------------------------
# Test 6: Float rounding
# ---------------------------------------------------------------------------
class TestFloatRounding:
    def test_totals_rounded_to_2_decimals(self):
        logs = [
            "ts | user_a | DEPOSIT | 100.555",
            "ts | user_b | DEPOSIT | 200.444",
        ]
        result = analyze_transaction_logs(logs)
        # 100.555 rounds to 100.56, 200.444 rounds to 200.44
        # total_volume should be round(100.56 + 200.44, 2) = 301.0
        # OR the implementation may round the sum: round(100.555 + 200.444, 2) = 301.0
        # Either way the total should be rounded to 2 decimals
        total = result["total_volume"]
        assert total == round(total, 2), "total_volume must be rounded to 2 decimal places"


# ---------------------------------------------------------------------------
# Test 7: Unique users sorted alphabetically
# ---------------------------------------------------------------------------
class TestUniqueUsersSorted:
    def test_alphabetical_order(self):
        logs = [
            "ts | user_zara | DEPOSIT | 10",
            "ts | user_adam | WITHDRAWAL | 20",
            "ts | user_mia | TRANSFER | 30",
            "ts | user_adam | DEPOSIT | 40",
        ]
        result = analyze_transaction_logs(logs)
        assert result["unique_users"] == ["user_adam", "user_mia", "user_zara"]


# ---------------------------------------------------------------------------
# Test 8: High value transactions sorted descending by amount
# ---------------------------------------------------------------------------
class TestHighValueSortOrder:
    def test_descending_sort(self):
        logs = [
            "ts | u1 | DEPOSIT | 500",
            "ts | u2 | WITHDRAWAL | 1000",
            "ts | u3 | TRANSFER | 750",
        ]
        result = analyze_transaction_logs(logs)
        hvt = result["high_value_transactions"]
        amounts = [t["amount"] for t in hvt]
        assert amounts == sorted(amounts, reverse=True)


# ---------------------------------------------------------------------------
# Test 9: Function never crashes — fuzz-like edge cases
# ---------------------------------------------------------------------------
class TestNeverCrashes:
    def test_none_in_list(self):
        """If someone passes non-string items, function should not crash."""
        try:
            analyze_transaction_logs(["valid | user | DEPOSIT | 100", None])  # type: ignore
        except TypeError:
            # Acceptable: TypeError on None is a reasonable Python behavior.
            # But if the function handles it gracefully, even better.
            pass

    def test_whitespace_only_fields(self):
        result = analyze_transaction_logs(["  |  |  |  "])
        assert result["corrupted_records"] == 1

    def test_extra_pipes(self):
        result = analyze_transaction_logs(["a | b | DEPOSIT | 100 | extra"])
        assert result["corrupted_records"] == 1
