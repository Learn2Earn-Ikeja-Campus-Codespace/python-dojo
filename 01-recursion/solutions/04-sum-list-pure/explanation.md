# Explanation: 04-sum-list-pure

## Why Index Pointers Matter
A common beginner mistake when writing recursive list operations is slicing:
```python
# INEFFICIENT:
return numbers[0] + sum_list(numbers[1:])
```
In Python, slicing a list creates a brand-new copy of the remaining elements.
- For a list of size $n$, the recursive calls make copies of size $n - 1, n - 2, \dots, 1$.
- Total memory allocated: $O(n^2)$.
- Total time spent copying: $O(n^2)$.

By passing an integer `index` and passing the same `numbers` reference along, each call only costs $O(1)$ time and $O(1)$ memory, reducing overall time complexity to $O(n)$ and space complexity to $O(n)$ stack frames.
