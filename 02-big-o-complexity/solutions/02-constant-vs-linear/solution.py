"""
Solution for Drill 02: Constant vs Linear Time Operations
Module: 02-big-o-complexity
"""


def get_extremes_constant(nums: list) -> tuple:
    """Returns (first, last) element in O(1) constant time."""
    if not nums:
        raise ValueError("nums list cannot be empty")
    return (nums[0], nums[-1])


def get_extremes_linear(nums: list) -> tuple:
    """Returns (first, last) element in O(n) linear scan time without direct indexing."""
    if not nums:
        raise ValueError("nums list cannot be empty")
    first = None
    last = None
    for i, x in enumerate(nums):
        if i == 0:
            first = x
        last = x
    return (first, last)
