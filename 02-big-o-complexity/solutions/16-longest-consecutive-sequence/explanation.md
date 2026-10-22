# Deep-Dive Explanation: 16-longest-consecutive-sequence

## 💡 Algorithmic Thinking

Sorting takes $O(n \log n)$, which violates the $O(n)$ constraint.
Using a hash set:
1. Insert all numbers into `num_set` ($O(n)$ time).
2. Only initiate a sequence count if `num - 1` is NOT in the set. This ensures we only explore from the true start of each consecutive streak.
3. Because each number is visited at most twice (once in the outer loop, once in the inner loop), total runtime is strictly linear $O(n)$.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$ to store elements in the hash set.
