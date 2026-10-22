# Drill 11: Fast Exponentiation ($O(\log n)$)

## Learning Target
Learn binary exponentiation (divide-and-conquer) to compute powers in logarithmic time.

$$x^n = \begin{cases} 1 & n = 0 \\ (x^2)^{n/2} & n \text{ is even} \\ x \times x^{n-1} & n \text{ is odd} \end{cases}$$

---

## Problem Statement

Write a function `power(base: int | float, exp: int) -> int | float` that recursively computes `base ** exp`.

Supports negative exponents: $x^{-n} = \frac{1}{x^n}$.

### Rules & Constraints:
1. Do not use `**`, `pow()`, or loops.
2. Must run in $O(\log |exp|)$ time.
3. If $base = 0$ and $exp < 0$, raise `ZeroDivisionError`.

---

## Examples

```python
power(2, 10)   # 1024
power(2, -3)   # 0.125
power(5, 0)    # 1
power(0, 5)    # 0
```
