"""
Solution for Drill 19: Subarrays Summing to K
Module: 02-big-o-complexity
"""


def subarray_sum(nums: list[int], k: int) -> int:
    """Counts contiguous subarrays summing to k in O(n) time and O(n) space."""
    prefix_counts = {0: 1}
    running_sum = 0
    count = 0

    for num in nums:
        running_sum += num
        target = running_sum - k
        if target in prefix_counts:
            count += prefix_counts[target]
        prefix_counts[running_sum] = prefix_counts.get(running_sum, 0) + 1

    return count
