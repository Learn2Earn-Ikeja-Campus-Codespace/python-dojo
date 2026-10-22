# Explanation: 05-count-occurrences

## Boolean Equality in Python
Python evaluates `1 == True` and `0 == False` to `True` because `bool` is a subclass of `int`.
When counting occurrences in generic lists that may contain booleans and numbers, a naive `items[index] == target` would treat `1` as matching `True`.

To prevent this:
```python
if isinstance(target, bool) or isinstance(current, bool):
    is_match = (current is target)
else:
    is_match = (current == target)
```

## Complexity
- **Time:** $O(n)$ where $n = \text{len}(items)$.
- **Space:** $O(n)$ recursive stack frames.
