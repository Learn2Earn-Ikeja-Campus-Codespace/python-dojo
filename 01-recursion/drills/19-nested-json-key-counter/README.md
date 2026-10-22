# Drill 19: Nested JSON Key Counter

## Learning Target
Traverse mixed, polymorphic JSON-style data structures containing dicts, lists, and primitives recursively.

---

## Problem Statement

Write a function `count_keys(data, target_key: str) -> int` that recursively counts every occurrence of `target_key` at any depth in a nested structure of dicts and lists.

### Rules & Constraints:
1. If current node is a `dict`, check its keys and recurse on its values.
2. If current node is a `list`, recurse through its elements.
3. If current node is primitive (int, str, bool, None), return `0`.

---

## Examples

```python
payload = {
    "id": 1,
    "user": {
        "id": 2,
        "tags": [{"id": 3}, {"id": 4}]
    }
}

count_keys(payload, "id")   # 4
count_keys(payload, "name") # 0
```
