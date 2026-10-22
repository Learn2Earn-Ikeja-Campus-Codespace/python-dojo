# Drill 03: Dependent Nested Loop Counting

## Learning Target
Understand why nested loops with dependent bounds run in $O(n^2)$ time:
$$\sum_{i=0}^{n-1} (n - 1 - i) = \frac{n(n - 1)}{2} \approx \frac{1}{2}n^2 \in O(n^2)$$

---

## Problem Statement

Write a function `count_unique_pairs(items: list) -> tuple[list[tuple], int]` that generates all unique 2-element combinations `(items[i], items[j])` where $i < j$.

Returns a tuple: `(list_of_pairs, operation_count)`.

### Rules & Constraints:
1. `operation_count` must track the exact number of times the inner comparison executes.
2. For $n = 5$, `operation_count` must be exactly $10$.
3. Time Complexity: $O(n^2)$, Auxiliary Space: $O(n^2)$ to hold result pairs.

---

## Examples

```python
pairs, count = count_unique_pairs([1, 2, 3])
# pairs = [(1, 2), (1, 3), (2, 3)]
# count = 3  (2 + 1)
```
