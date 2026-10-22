# Drill 14: Generate All Subsets (Power Set)

## Learning Target
Master the fundamental include/exclude binary decision tree pattern in backtracking.

---

## Problem Statement

Write a function `subsets(nums: list[int], index: int = 0) -> list[list[int]]` that recursively generates all subsets of unique elements in `nums`.

### Rules & Constraints:
1. Do not use `itertools` or loops.
2. For $n$ items, returns exactly $2^n$ subsets.
3. Empty list `[]` returns `[[]]`.

---

## Examples

```python
subsets([1, 2])     # [[], [2], [1], [1, 2]] (order may vary)
subsets([])         # [[]]
subsets([5])        # [[], [5]]
```
