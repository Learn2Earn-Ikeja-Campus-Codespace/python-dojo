# Drill 08: Intersection of Two Arrays ($O(m + n)$)

## Learning Target
Learn to compute intersections between lists of sizes $m$ and $n$ in $O(m + n)$ time instead of naive $O(m \times n)$.

---

## Problem Statement

Write `intersection(a: list, b: list) -> list`:
- Returns a list containing the unique elements present in both `a` and `b`.
- Must run in $O(m + n)$ time using set conversion.

---

## Examples

```python
intersection([1, 2, 2, 1], [2, 2])  # [2]
intersection([4, 9, 5], [9, 4, 9, 8, 4])  # [4, 9] (order may vary)
```
