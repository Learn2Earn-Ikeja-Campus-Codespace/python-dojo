# Drill 05: Space Complexity Audit (In-Place vs Allocation)

## Learning Target
Differentiate algorithms that allocate $O(n)$ auxiliary memory from algorithms that modify data in-place with $O(1)$ auxiliary space.

---

## Problem Statement

Write two functions to reverse a list:

1. `reverse_with_allocation(nums: list) -> list`:
   - Returns a new reversed list.
   - Auxiliary Space: $O(n)$
   - Does NOT mutate the input `nums`.
2. `reverse_in_place(nums: list) -> None`:
   - Reverses `nums` **in-place** using two pointers.
   - Auxiliary Space: $O(1)$
   - Modifies `nums` directly; returns `None`.

---

## Examples

```python
a = [1, 2, 3]
b = reverse_with_allocation(a)
# b = [3, 2, 1], a is still [1, 2, 3]

reverse_in_place(a)
# a is now [3, 2, 1]
```
