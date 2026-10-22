# Drill 16: Climbing Stairs (1, 2, or 3 Steps)

## Learning Target
Model state transitions in multi-way decision trees with memoization.

---

## Problem Statement

You are climbing a staircase with $n$ steps. At each step, you can climb **1, 2, or 3 steps**.

Write a function `count_ways(n: int, memo: dict | None = None) -> int` that returns the number of distinct ways to reach the top.

### Rules & Constraints:
1. Do not use loops.
2. For $n < 0$, return `0`.
3. For $n = 0$, return `1` (standing at ground level counts as 1 way).
4. Must handle $n = 30$ quickly via memoization.

---

## Examples

```python
count_ways(1)  # 1: [1]
count_ways(2)  # 2: [1+1, 2]
count_ways(3)  # 4: [1+1+1, 1+2, 2+1, 3]
count_ways(4)  # 7
```
