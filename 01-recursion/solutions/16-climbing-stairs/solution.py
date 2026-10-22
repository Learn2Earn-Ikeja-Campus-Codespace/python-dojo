"""
Solution for Drill 16: Climbing Stairs
Module: 01-recursion
"""


def count_ways(n: int, memo: dict | None = None) -> int:
    """
    Counts ways to climb n stairs taking 1, 2, or 3 steps.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    memo[n] = count_ways(n - 1, memo) + count_ways(n - 2, memo) + count_ways(n - 3, memo)
    return memo[n]
