# Drill 19: Subarrays Summing to K ($O(n)$ Time)

## Learning Target
Learn to use prefix sum frequencies to count subarrays summing to $k$ in $O(n)$ time instead of inspecting all $O(n^2)$ subarray bounds.

---

## Problem Statement

Write `subarray_sum(nums: list[int], k: int) -> int`:
- Returns the total number of continuous subarrays whose sum equals $k$.
- Time Complexity: $O(n)$
- Auxiliary Space: $O(n)$

---

## Examples

```python
subarray_sum([1, 1, 1], 2)       # 2 ([1,1] at index 0..1 and 1..2)
subarray_sum([1, 2, 3], 3)       # 2 ([1,2] and [3])
subarray_sum([1, -1, 0], 0)      # 3 ([1, -1], [0], [1, -1, 0])
```
