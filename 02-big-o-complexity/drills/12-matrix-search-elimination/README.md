# Drill 12: Sorted Matrix Search Elimination ($O(m + n)$)

## Learning Target
Understand how starting search from the top-right corner of a row-and-column sorted matrix eliminates an entire row or column in each step, achieving $O(m + n)$ instead of $O(m \times n)$.

---

## Problem Statement

Write `search_matrix(matrix: list[list[int]], target: int) -> bool`:
- Matrix has integers sorted in ascending order from left to right in each row.
- Matrix has integers sorted in ascending order from top to bottom in each column.
- Returns `True` if `target` exists, else `False`.
- Must run in $O(m + n)$ time where $m$ is rows, $n$ is columns.

---

## Examples

```python
matrix = [
  [1,   4,  7, 11],
  [2,   5,  8, 12],
  [3,   6,  9, 16],
  [10, 13, 14, 17]
]

search_matrix(matrix, 5)   # True
search_matrix(matrix, 20)  # False
```
