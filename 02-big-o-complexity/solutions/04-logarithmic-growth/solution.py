"""
Solution for Drill 04: Logarithmic Growth
Module: 02-big-o-complexity
"""


def count_divisions(n: int) -> int:
    """Returns the number of times n can be divided by 2 until it reaches 1."""
    if n <= 0:
        raise ValueError("n must be a positive integer > 0")
    divisions = 0
    curr = n
    while curr > 1:
        curr //= 2
        divisions += 1
    return divisions
