"""
Solution for Drill 14: Generate All Subsets
Module: 01-recursion
"""


def subsets(nums: list[int], index: int = 0) -> list[list[int]]:
    """
    Recursively generates all 2^n subsets using include/exclude branching.
    """
    if index >= len(nums):
        return [[]]

    # Subsets without current element
    without_current = subsets(nums, index + 1)

    # Subsets with current element prepended
    current = nums[index]
    with_current = [[current] + s for s in without_current]

    return without_current + with_current
