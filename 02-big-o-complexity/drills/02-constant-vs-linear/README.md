# Drill 02: Constant vs Linear Time Operations

## Learning Target
Learn to distinguish between $O(1)$ operations (array index access, dict key lookup, length check) and $O(n)$ operations (linear scan, array slicing, list `.insert(0, val)`).

---

## Problem Statement

Implement two functions that return the first and last element of a non-empty list:

1. `get_extremes_constant(nums: list) -> tuple`:
   - Must run in strictly $O(1)$ time and $O(1)$ space.
   - Raises `ValueError` if `nums` is empty.
2. `get_extremes_linear(nums: list) -> tuple`:
   - Traverses the elements sequentially in $O(n)$ time to find first and last without direct index subscription.
   - Raises `ValueError` if `nums` is empty.

---

## Examples

```python
get_extremes_constant([10, 20, 30])  # (10, 30)
get_extremes_linear([5, 8, 12, 99])   # (5, 99)
```
