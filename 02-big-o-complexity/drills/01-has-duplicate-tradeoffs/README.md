# Drill 01: Duplicate Detection & The 3 Classical Trade-offs

## Learning Target
Understand the foundational Quest 2 from the Elite Challenge: the engineering trade-offs between Time, Memory (Auxiliary Space), and Input Mutation.

---

## Problem Statement

Implement three different approaches to determine if a list contains any duplicate values:

1. `has_duplicate_quadratic(items: list) -> bool`:
   - Brute-force approach using nested loops.
   - Time Complexity: $O(n^2)$
   - Auxiliary Space: $O(1)$
2. `has_duplicate_hash(items: list) -> bool`:
   - Early-exit approach using a tracking hash set.
   - Time Complexity: Expected $O(n)$
   - Auxiliary Space: $O(n)$
3. `has_duplicate_sorted(items: list) -> bool`:
   - Sort-and-scan adjacent approach.
   - Time Complexity: $O(n \log n)$
   - Auxiliary Space: $O(n)$ (because Python's `sorted()` creates a new list)

---

## Examples

```python
has_duplicate_quadratic([1, 2, 3, 2])  # True
has_duplicate_hash([1, 2, 3, 4])       # False
has_duplicate_sorted([5, 5])           # True
```
