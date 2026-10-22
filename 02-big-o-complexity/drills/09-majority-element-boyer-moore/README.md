# Drill 09: Boyer-Moore Majority Vote ($O(n)$ Time, $O(1)$ Space)

## Learning Target
Upgrade an algorithm from $O(n)$ space (frequency dictionary) down to $O(1)$ auxiliary space using the Boyer-Moore voting algorithm.

A majority element appears more than $\lfloor n/2 \rfloor$ times.

---

## Problem Statement

Write `majority_element(nums: list[int]) -> int`:
- Finds the majority element.
- Time Complexity: $O(n)$
- Auxiliary Space: strictly $O(1)$ (no dictionaries, no sets, no list counters).

---

## Examples

```python
majority_element([3, 2, 3])        # 3
majority_element([2, 2, 1, 1, 1, 2, 2]) # 2
```
