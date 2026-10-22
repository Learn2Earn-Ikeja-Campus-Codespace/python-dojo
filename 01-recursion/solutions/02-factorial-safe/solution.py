"""
Solution for Drill 02: Safe Factorial
Module: 01-recursion
"""


def factorial(n: int) -> int:
    """
    Recursively calculates n! with strict domain checking.
    """
    # Guard against booleans and non-integers
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer")

    # Guard against negative integers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    # Base case: 0! = 1
    if n == 0:
        return 1

    # Recursive step
    return n * factorial(n - 1)
