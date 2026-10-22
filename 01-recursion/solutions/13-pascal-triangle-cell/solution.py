"""
Solution for Drill 13: Pascal Triangle Cell
Module: 01-recursion
"""


def pascal(row: int, col: int, memo: dict | None = None) -> int:
    """
    Recursively computes cell value in Pascal's Triangle.
    """
    if row < 0:
        raise ValueError("row must be non-negative")
    if col < 0 or col > row:
        return 0
    if col == 0 or col == row:
        return 1

    if memo is None:
        memo = {}

    key = (row, col)
    if key in memo:
        return memo[key]

    memo[key] = pascal(row - 1, col - 1, memo) + pascal(row - 1, col, memo)
    return memo[key]
