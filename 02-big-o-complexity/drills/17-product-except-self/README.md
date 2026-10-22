# Drill 17: Product of Array Except Self ($O(n)$ Time, $O(1)$ Extra Space)

## Learning Target
Learn prefix and suffix product passes without using division. Achieve $O(n)$ runtime and $O(1)$ auxiliary space (output array does not count as auxiliary space).

---

## Problem Statement

Write `product_except_self(nums: list[int]) -> list[int]`:
- Returns an array `output` where `output[i]` is the product of all elements in `nums` except `nums[i]`.
- Constraints: Do NOT use division `/` or `//`. Must run in $O(n)$ time.

---

## Examples

```python
product_except_self([1, 2, 3, 4])  # [24, 12, 8, 6]
product_except_self([-1, 1, 0, -3, 3]) # [0, 0, 9, 0, 0]
```
