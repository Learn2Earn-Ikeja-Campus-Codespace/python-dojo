# Drill 20: Empirical Growth Rate Benchmark Harness

## Learning Target
Bridge mathematical Big O theory with empirical execution reality. Build an automated benchmark harness that times an algorithm across input sizes $n_1, n_2, \dots$, detects whether the curve is linear or quadratic, and prints the empirical growth multiplier.

---

## Problem Statement

Write `measure_growth_ratio(fn, n1: int, n2: int) -> float`:
- Times execution of `fn(list(range(n1)))` vs `fn(list(range(n2)))`.
- Returns the ratio: $\frac{T(n2)}{T(n1)}$.
- For $n2 = 2 \times n1$:
  - A linear $O(n)$ algorithm will have a ratio $\approx 2.0$.
  - A quadratic $O(n^2)$ algorithm will have a ratio $\approx 4.0$ ($2^2$).

---

## Examples

```python
def linear_sum(lst): return sum(lst)
def quadratic_pairs(lst): return [(a, b) for a in lst for b in lst]

ratio_lin = measure_growth_ratio(linear_sum, 1000, 2000)      # ~ 2.0
ratio_quad = measure_growth_ratio(quadratic_pairs, 500, 1000)  # ~ 4.0
```
