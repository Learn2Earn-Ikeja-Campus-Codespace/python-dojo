# Drill 13: Pascal's Triangle Cell

## Learning Target
Understand 2D coordinate recurrence relations:
$$C(r, c) = C(r - 1, c - 1) + C(r - 1, c)$$
where $C(r, 0) = 1$ and $C(r, r) = 1$.

---

## Problem Statement

Write a function `pascal(row: int, col: int, memo: dict | None = None) -> int` that recursively computes the value at 0-based `row` and `col` of Pascal's triangle.

### Rules & Constraints:
1. Do not use loops, factorials, or combinations formulas.
2. If `col < 0` or `col > row`, return `0`.
3. If `row < 0`, raise `ValueError`.
4. Uses memoization so `pascal(30, 15)` evaluates in milliseconds.

---

## Examples

```python
pascal(0, 0)  # 1
pascal(4, 2)  # 6
pascal(4, 0)  # 1
pascal(4, 4)  # 1
```
