"""
Solution for Drill 05: Space Complexity Audit
Module: 02-big-o-complexity
"""


def reverse_with_allocation(nums: list) -> list:
    """Returns a reversed copy of nums using O(n) auxiliary space."""
    return [nums[i] for i in range(len(nums) - 1, -1, -1)]


def reverse_in_place(nums: list) -> None:
    """Reverses nums in-place using O(1) auxiliary space."""
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
