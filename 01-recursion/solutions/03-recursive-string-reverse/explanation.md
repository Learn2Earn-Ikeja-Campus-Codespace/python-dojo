# Explanation: 03-recursive-string-reverse

## Structural Decomposition
A string of length $n$ can be decomposed into:
- The last character: `text[-1]`
- The preceding prefix of length $n - 1$: `text[:-1]`

The reversed string is simply `text[-1] + reverse_string(text[:-1])`.

Alternatively, head recursion works identically:
`reverse_string(text[1:]) + text[0]`

## Complexity Analysis
- **Time Complexity:** $O(n^2)$
  In Python, strings are immutable. Slicing a string `text[:-1]` creates a new string copy of length $k$, costing $O(k)$ time. Across all $n$ recursive steps:
  $$(n - 1) + (n - 2) + \dots + 1 = \frac{n(n - 1)}{2} \implies O(n^2)$$
- **Auxiliary Space:** $O(n)$ stack frames, plus $O(n^2)$ total intermediate substring allocations if not garbage-collected immediately.
