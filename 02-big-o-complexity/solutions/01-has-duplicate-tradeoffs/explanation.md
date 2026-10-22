# Deep-Dive Explanation: 01-has-duplicate-tradeoffs

## 💡 Algorithmic Thinking

Duplicate detection highlights the classic time-versus-space engineering trade-off:

1. **Quadratic Brute-Force ($O(n^2)$ time, $O(1)$ auxiliary space)**:
   Compare each item against every subsequent item. No memory allocation is needed, making it suitable for memory-constrained embedded environments with tiny lists.

2. **Hash Set Strategy ($O(n)$ average time, $O(n)$ space)**:
   Traverse the sequence once while maintaining a hash set of observed elements. Membership testing is $O(1)$ on average. This is the industry-standard general-purpose choice.

3. **Sorted Adjacent Comparison ($O(n \log n)$ time, $O(n)$ space in Timsort)**:
   Sorting brings duplicates together. Scanning adjacent pairs requires a single linear pass. Useful when data arrives pre-sorted or must be sorted anyway.

---

## 📊 Complexity Comparison Matrix

| Approach | Time Complexity | Auxiliary Space | Mutation |
| :--- | :--- | :--- | :--- |
| `has_duplicate_quadratic` | $O(n^2)$ | $O(1)$ | No |
| `has_duplicate_hash` | $O(n)$ | $O(n)$ | No |
| `has_duplicate_sorted` | $O(n \log n)$ | $O(n)$ | No |
