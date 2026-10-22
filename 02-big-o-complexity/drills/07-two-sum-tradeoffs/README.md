# Drill 07: Two Sum Algorithmic Trade-offs

## Learning Target
Compare the classic algorithm across three different Big O profiles:
1. Brute Force: $O(n^2)$ time, $O(1)$ space.
2. Hash Map: $O(n)$ time, $O(n)$ space.
3. Two-Pointer on Sorted: $O(n)$ time, $O(1)$ space.

---

## Problem Statement

Write `two_sum_hash(nums: list[int], target: int) -> tuple[int, int] | None`:
- Returns the 0-based indices `(i, j)` where `nums[i] + nums[j] == target`.
- Returns `None` if no pair exists.
- Must run in $O(n)$ time using a hash map for complement lookup.

---

## Examples

```python
two_sum_hash([2, 7, 11, 15], 9)  # (0, 1)
two_sum_hash([3, 2, 4], 6)        # (1, 2)
two_sum_hash([3, 3], 6)           # (0, 1)
two_sum_hash([1, 2], 5)           # None
```
