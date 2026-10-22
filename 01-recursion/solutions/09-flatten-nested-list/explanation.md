# Explanation: 09-flatten-nested-list

## Structural Recursion on Tree Sequences
A nested list is fundamentally an arbitrary tree:
- If `item` is a leaf (not a list), wrap it in a list: `[item]`.
- If `item` is an internal subtree (a list), recursively flatten it: `flatten(item)`.
Combine the flattened current item with the flattened remainder of the list.
