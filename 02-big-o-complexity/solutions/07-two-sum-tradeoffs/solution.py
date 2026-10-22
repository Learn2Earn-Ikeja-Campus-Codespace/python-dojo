"""
Solution for Drill 07: Two Sum Hash
Module: 02-big-o-complexity
"""


def two_sum_hash(nums: list[int], target: int) -> tuple[int, int] | None:
    """Finds two indices whose values sum to target in O(n) time and O(n) space."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None
