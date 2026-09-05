"""
Diagnostic Challenge #1 — Transaction Log Analyzer

Problem statement: 00_setup/diagnostics/problems/transaction_log_analyzer.md
Tests: 00_setup/diagnostics/tests/test_transaction_log_analyzer.py

Run tests:
    python -m pytest 00_setup/diagnostics/tests/test_transaction_log_analyzer.py -v

YOUR TASK:
    Implement the analyze_transaction_logs function below.
    Read the problem statement for full requirements.
    Do NOT change the function signature.
"""


def analyze_transaction_logs(raw_logs: list[str]) -> dict:
    """Analyze raw transaction log strings and return aggregated metrics.

    Args:
        raw_logs: List of pipe-delimited transaction strings.
                  Format: "<timestamp> | <user_id> | <transaction_type> | <amount>"

    Returns:
        Dictionary containing:
            - total_records
            - valid_records
            - corrupted_records
            - total_volume
            - breakdown_by_type
            - high_value_transactions
            - unique_users
    """
    # TODO: Implement your solution here
    pass
