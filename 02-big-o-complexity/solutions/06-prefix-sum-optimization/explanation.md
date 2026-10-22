# Deep-Dive Explanation: 06-prefix-sum-optimization

## 💡 Algorithmic Thinking

A naive range sum iterates from `left` to `right`, requiring $O(k)$ time per query (worst case $O(n)$). For $Q$ queries, total runtime is $O(Q \cdot n)$.

By precomputing prefix sums where:
$$\text{prefix}[i] = \sum_{k=0}^{i-1} \text{nums}[k]$$

Any subsegment sum from index $L$ to $R$ can be calculated in $O(1)$:
$$\text{sum}(L, R) = \text{prefix}[R + 1] - \text{prefix}[L]$$

---

## 📊 Complexity Analysis

- **Preprocessing Time**: $O(n)$
- **Query Time**: $O(1)$
- **Auxiliary Space**: $O(n)$ for prefix array.
