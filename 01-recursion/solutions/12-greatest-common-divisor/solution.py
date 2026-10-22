"""
Solution for Drill 12: Greatest Common Divisor
Module: 01-recursion
"""


def gcd(a: int, b: int) -> int:
    """
    Recursively calculates greatest common divisor using Euclidean algorithm.
    """
    if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Arguments must be integers")

    a, b = abs(a), abs(b)

    if b == 0:
        return a

    return gcd(b, a % b)
