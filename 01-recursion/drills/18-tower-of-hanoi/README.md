# Drill 18: Tower of Hanoi Move Generator

## Learning Target
Understand the quintessential divide-and-conquer strategy:
1. Move $n-1$ disks from source to auxiliary.
2. Move largest disk $n$ directly from source to target.
3. Move $n-1$ disks from auxiliary to target.

---

## Problem Statement

Write a function `hanoi(n: int, source: str = "A", target: str = "C", auxiliary: str = "B") -> list[tuple[str, str]]` that recursively generates the optimal sequence of moves.

Each move is a tuple `(from_peg, to_peg)`.

### Rules & Constraints:
1. Optimal solution requires exactly $2^n - 1$ moves.
2. Base case: $n = 0$ returns `[]`.
3. If $n < 0$, raise `ValueError`.

---

## Examples

```python
hanoi(1, "A", "C", "B")  # [("A", "C")]
hanoi(2, "A", "C", "B")  # [("A", "B"), ("A", "C"), ("B", "C")]
```
