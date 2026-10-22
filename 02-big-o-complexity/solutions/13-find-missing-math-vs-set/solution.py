"""
Solution for Drill 13: Find Missing Number
Module: 02-big-o-complexity
"""


def find_missing_number(nums: list[int]) -> int:
    """Finds the missing number from [0..n] in O(n) time and O(1) space."""
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)
