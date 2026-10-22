"""
Solution for Drill 11: Fast Exponentiation
Module: 01-recursion
"""


def power(base: int | float, exp: int) -> int | float:
    """
    Recursively calculates base ** exp in O(log exp) time.
    """
    if isinstance(exp, bool) or not isinstance(exp, int):
        raise TypeError("exp must be an integer")

    if base == 0 and exp < 0:
        raise ZeroDivisionError("0 cannot be raised to a negative power")

    if exp == 0:
        return 1

    if exp < 0:
        return 1.0 / power(base, -exp)

    half = power(base, exp // 2)

    if exp % 2 == 0:
        return half * half
    else:
        return base * half * half
