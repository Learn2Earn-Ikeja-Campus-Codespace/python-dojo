"""
Solution for Drill 09: Boyer-Moore Majority Vote
Module: 02-big-o-complexity
"""


def majority_element(nums: list[int]) -> int:
    """Finds majority element (> n // 2) in O(n) time and O(1) space."""
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
