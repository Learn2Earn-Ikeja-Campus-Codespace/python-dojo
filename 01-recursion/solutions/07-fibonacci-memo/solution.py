"""
Solution for Drill 07: Fibonacci with Memoization
Module: 01-recursion
"""


def fibonacci(n: int, memo: dict | None = None) -> int:
    """
    Recursively computes the n-th Fibonacci number using memoization.
    Time Complexity: O(n)
    Auxiliary Space: O(n)
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
