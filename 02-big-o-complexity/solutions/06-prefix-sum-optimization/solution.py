"""
Solution for Drill 06: Prefix Sum Optimization
Module: 02-big-o-complexity
"""


class RangeSumQuery:
    """Precomputes cumulative prefix sums to answer range queries in O(1) time."""

    def __init__(self, nums: list[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def query(self, left: int, right: int) -> int:
        """Returns sum of elements between indices left and right inclusive in O(1)."""
        return self.prefix[right + 1] - self.prefix[left]
