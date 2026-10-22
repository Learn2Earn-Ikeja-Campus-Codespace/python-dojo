# Explanation: 10-nested-dict-lookup

## Hierarchical Key-Path Descent
At each level $i$:
1. Check if the current node is a `dict` and contains `keys[i]`.
2. If it's the last key in the path (`index == len(keys) - 1`), return the value immediately.
3. Otherwise, step into `data[key]` and recurse with `index + 1`.
