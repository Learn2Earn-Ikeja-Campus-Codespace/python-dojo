# Drill 10: Deep Nested Dictionary Lookup

## Learning Target
Learn to traverse hierarchical, key-value tree structures using key-path recursion.

---

## Problem Statement

Write a function `deep_get(data: dict, keys: list[str], index: int = 0)` that retrieves a nested value by traversing a sequence of keys.

Returns `None` if any key in the path does not exist or if the current node is not a dictionary.

### Rules & Constraints:
1. Do not use loops.
2. If `data` is not a dict on the initial call, raise `TypeError("data must be a dict")`.
3. If `keys` is empty, return `None`.

---

## Examples

```python
data = {
    "user": {
        "profile": {
            "name": "Maadan",
            "score": 100
        }
    }
}

deep_get(data, ["user", "profile", "name"])   # "Maadan"
deep_get(data, ["user", "settings", "theme"]) # None
deep_get(data, [])                           # None
```
