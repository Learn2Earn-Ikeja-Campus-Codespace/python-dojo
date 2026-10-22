# Drill 10: In-Place Sorted Array Merge ($O(1)$ Space)

## Learning Target
Master reverse three-pointer iteration to merge two sorted arrays into one in $O(m + n)$ time without allocating an extra array ($O(1)$ auxiliary space).

---

## Problem Statement

Given two sorted integer arrays `nums1` and `nums2`, merge `nums2` into `nums1` in-place.

`nums1` has a length of $m + n$, where the first $m$ elements denote the sorted content, and the last $n$ elements are initialized to $0$ and must be overwritten.

Write `merge_inplace(nums1: list[int], m: int, nums2: list[int], n: int) -> None`.

---

## Examples

```python
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge_inplace(nums1, 3, nums2, 3)
# nums1 is now [1, 2, 2, 3, 5, 6]
```
