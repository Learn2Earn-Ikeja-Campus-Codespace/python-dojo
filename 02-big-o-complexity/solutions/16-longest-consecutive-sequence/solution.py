"""
Solution for Drill 16: Longest Consecutive Sequence
Module: 02-big-o-complexity
"""


def longest_consecutive(nums: list[int]) -> int:
    """Finds length of longest consecutive elements sequence in O(n) time and O(n) space."""
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        # Check if num is the start of a streak
        if num - 1 not in num_set:
            curr = num
            curr_len = 1
            while curr + 1 in num_set:
                curr += 1
                curr_len += 1
            if curr_len > max_len:
                max_len = curr_len

    return max_len
