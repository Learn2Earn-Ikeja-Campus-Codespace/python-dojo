# Explanation: 19-nested-json-key-counter

## Polymorphic Traversal
Inspect type of current node:
- If `dict`: check each key, then recurse on every value.
- If `list`: iterate and recurse on each item.
- Primitives terminate naturally and return 0.
