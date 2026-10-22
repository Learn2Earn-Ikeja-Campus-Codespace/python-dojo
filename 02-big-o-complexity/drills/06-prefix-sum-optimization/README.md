# Drill 06: Prefix Sum Optimization ($O(n) \to O(1)$ Query)

## Learning Target
Learn the precomputation pattern: spending $O(n)$ time and $O(n)$ space once during preprocessing to reduce subsequent range-sum queries from $O(k)$ to $O(1)$!

---

## Problem Statement

Implement `RangeSumQuery`:
- `__init__(nums: list[int])`: Precomputes running prefix sums in $O(n)$ time.
- `query(left: int, right: int) -> int`: Computes the sum of elements from index `left` to `right` (inclusive) in strictly $O(1)$ time!

$$\text{sum}(left, right) = \text{prefix}[right + 1] - \text{prefix}[left]$$

---

## Examples

```python
rsq = RangeSumQuery([1, 2, 3, 4, 5])
rsq.query(1, 3)  # 9 (2 + 3 + 4)
rsq.query(0, 4)  # 15 (1 + 2 + 3 + 4 + 5)
rsq.query(2, 2)  # 3
```
