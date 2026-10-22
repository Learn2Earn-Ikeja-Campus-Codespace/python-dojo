"""
Solution for Drill 10: In-Place Merge
Module: 02-big-o-complexity
"""


def merge_inplace(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """Merges nums2 into nums1 in-place in O(m + n) time and O(1) space."""
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
