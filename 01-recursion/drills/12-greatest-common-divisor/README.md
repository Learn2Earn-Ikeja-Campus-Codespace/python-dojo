# Drill 12: Euclidean Greatest Common Divisor (GCD)

## Learning Target
Implement the Euclidean algorithm via pure recurrence relation:
$$\gcd(a, b) = \gcd(b, a \pmod b), \quad \gcd(a, 0) = |a|$$

---

## Problem Statement

Write a function `gcd(a: int, b: int) -> int` that recursively calculates the greatest common divisor of two integers.

### Rules & Constraints:
1. Do not use `math.gcd` or loops.
2. Works for positive and negative integers (result is always non-negative).
3. If inputs are not integers (or are booleans), raise `TypeError`.

---

## Examples

```python
gcd(48, 18)   # 6
gcd(101, 10)  # 1
gcd(-24, 60)  # 12
gcd(0, 5)     # 5
```
