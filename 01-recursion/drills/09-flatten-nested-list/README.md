# Drill 09: Flatten Arbitrarily Nested List

## Learning Target
Understand structural recursion on tree-like, heterogeneously nested sequences.

---

## Problem Statement

Write a function `flatten(nested: list) -> list` that recursively flattens a list containing integers and arbitrarily deeply nested lists into a single flat list.

### Rules & Constraints:
1. Do not use external libraries.
2. If `nested` is not a list, raise `TypeError("Input must be a list")`.
3. Handles empty lists and empty inner lists cleanly.

---

## Examples

```python
flatten([1, [2, [3, 4], 5], 6])  # [1, 2, 3, 4, 5, 6]
flatten([[[]], []])              # []
flatten([1, 2, 3])                # [1, 2, 3]
flatten([])                       # []
```
