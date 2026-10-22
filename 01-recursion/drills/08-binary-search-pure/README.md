# Drill 08: Pure Recursive Binary Search

## Learning Target
Master divide-and-conquer recursion with index pointers (`low`, `high`) to achieve $O(\log n)$ runtime without allocating array slices.

---

## Problem Statement

Write a function `binary_search(arr: list[int], target: int, low: int = 0, high: int | None = None) -> int` that recursively searches for `target` in a **sorted list** of unique integers.

Returns the 0-based index of `target`, or `-1` if not found.

### Rules & Constraints:
1. Do not use loops, `.index()`, `in` operator, or list slicing.
2. Must run in $O(\log n)$ time by halving search bounds on each step.
3. If `arr` is not a list, raise `TypeError("arr must be a list")`.
4. If `target` is not an int (or is a `bool`), raise `TypeError("target must be an integer")`.

---

## Examples

```python
binary_search([1, 3, 5, 7, 9, 11], 7)   # 3
binary_search([1, 3, 5, 7, 9, 11], 4)   # -1
binary_search([], 5)                    # -1
binary_search([10], 10)                 # 0
```
