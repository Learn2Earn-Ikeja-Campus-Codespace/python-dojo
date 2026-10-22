# Explanation: 08-binary-search-pure

## Why Pointers Avoid $O(n)$ Memory Slicing
If you slice the list (`arr[:mid]`), Python creates a new list copy of size $n/2$, costing $O(n)$ time and destroying the logarithmic runtime.

By passing integer indices `low` and `high`, no copies are made. At each call:
- The search window $[low, high]$ is cut in half.
- Total calls before window size reaches 0 is $\lfloor \log_2 n \rfloor + 1$.
- Time Complexity: $O(\log n)$.
- Auxiliary Space: $O(\log n)$ stack frames.
