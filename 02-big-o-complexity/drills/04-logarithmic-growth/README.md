# Drill 04: Logarithmic Growth ($O(\log n)$)

## Learning Target
Understand why halving a problem space at each step produces logarithmic growth ($	ext{steps} = \lfloor \log_2 n \rfloor + 1$).

---

## Problem Statement

Write a function `count_divisions(n: int) -> int` that counts how many times a positive integer $n$ can be divided by 2 (using integer floor division `// 2`) until it reaches $1$.

### Rules & Constraints:
1. If $n \le 0$, raise `ValueError("n must be positive")`.
2. Must run in $O(\log n)$ time.
3. For $n = 1024$, returns exactly $10$ divisions ($2^{10} = 1024$).
4. For $n = 1,000,000$, completes in $\approx 20$ iterations.

---

## Examples

```python
count_divisions(1)     # 0
count_divisions(2)     # 1
count_divisions(8)     # 3
count_divisions(1024)  # 10
```
