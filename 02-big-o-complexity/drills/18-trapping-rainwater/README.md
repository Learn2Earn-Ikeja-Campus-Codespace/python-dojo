# Drill 18: Trapping Rain Water ($O(n)$ Time, $O(1)$ Space)

## Learning Target
Upgrade 2D elevation trapping from $O(n)$ auxiliary memory (left/right max arrays) to two-pointer convergence in $O(1)$ auxiliary space.

---

## Problem Statement

Given $n$ non-negative integers representing an elevation map where the width of each bar is 1, write:

`trap(height: list[int]) -> int`:
- Computes how much water it can trap after raining.
- Time Complexity: $O(n)$
- Auxiliary Space: $O(1)$ (two-pointer approach).

---

## Examples

```python
trap([0,1,0,2,1,0,1,3,2,1,2,1])  # 6
trap([4,2,0,3,2,5])              # 9
trap([])                         # 0
```
