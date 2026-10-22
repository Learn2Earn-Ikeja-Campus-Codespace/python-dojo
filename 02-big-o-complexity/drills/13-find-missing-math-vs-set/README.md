# Drill 13: Gauss Formula vs Set Difference ($O(1)$ Space)

## Learning Target
Learn to use mathematical invariants (e.g. Gauss summation $\frac{n(n+1)}{2}$) to solve search problems in $O(1)$ auxiliary space instead of $O(n)$ hash sets.

---

## Problem Statement

Given an array `nums` containing $n$ distinct numbers in the range $[0, n]$, write:

`find_missing_number(nums: list[int]) -> int`:
- Finds the only number missing from the range.
- Time Complexity: $O(n)$
- Auxiliary Space: strictly $O(1)$ (no sets, no sorting).

---

## Examples

```python
find_missing_number([3, 0, 1])          # 2
find_missing_number([0, 1])             # 2
find_missing_number([9,6,4,2,3,5,7,0,1]) # 8
```
