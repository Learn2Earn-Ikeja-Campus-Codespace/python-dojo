# Drill 14: Dynamic Array Amortized Analysis

## Learning Target
Understand why Python's `list.append` runs in **amortized $O(1)$** time despite intermittent $O(n)$ array resize copies.

When the array fills its capacity $C$, it allocates a new buffer of size $2C$ and copies all elements over.

---

## Problem Statement

Implement `DynamicArraySimulator`:
- `__init__(initial_capacity: int = 2)`
- `append(value)`: Appends value. If size exceeds capacity, doubles capacity and increments `copy_operations` by current size.
- Tracks `total_appends` and `copy_operations`.
- Shows that average copy cost per element is $\le 2$ (proving amortized $O(1)$).

---

## Examples

```python
arr = DynamicArraySimulator(initial_capacity=2)
arr.append(1)  # size=1, cap=2, copies=0
arr.append(2)  # size=2, cap=2, copies=0
arr.append(3)  # size=3, cap=4, copies=2 (elements 1, 2 copied)
```
