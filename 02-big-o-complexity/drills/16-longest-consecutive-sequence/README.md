# Drill 16: Longest Consecutive Sequence ($O(n)$ Time)

## Learning Target
Learn the intelligent skip technique: by only initiating a counting sequence when an element has no left neighbor (`num - 1 not in set`), each element is visited at most twice, achieving $O(n)$ time despite an inner `while` loop!

---

## Problem Statement

Write `longest_consecutive(nums: list[int]) -> int`:
- Finds the length of the longest consecutive elements sequence.
- Time Complexity: strictly $O(n)$ (sorting is forbidden as it would take $O(n \log n)$).

---

## Examples

```python
longest_consecutive([100, 4, 200, 1, 3, 2])  # 4 ([1, 2, 3, 4])
longest_consecutive([0,3,7,2,5,8,4,6,0,1])   # 9 ([0, 1, 2, 3, 4, 5, 6, 7, 8])
longest_consecutive([])                      # 0
```
