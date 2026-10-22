# Deep-Dive Explanation: 13-find-missing-math-vs-set

## 💡 Algorithmic Thinking

Given $n$ distinct numbers in range $[0, n]$, exactly one number is missing.
- Gauss's summation formula gives the exact sum of numbers from 0 to $n$:
  $$S = \frac{n(n + 1)}{2}$$
- Subtracting the actual array sum from $S$ directly yields the missing number.
- No set, hash table, or sorting is required.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(n)$ single pass to sum the array.
- **Space Complexity**: $O(1)$ auxiliary space.
