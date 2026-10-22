# Deep-Dive Explanation: 03-nested-loop-counting

## 💡 Algorithmic Thinking

When the inner loop boundary depends on the outer loop index (`for j in range(i + 1, n)`), the number of inner iterations decreases each round:

$$\sum_{i=0}^{n-1} (n - 1 - i) = (n - 1) + (n - 2) + \dots + 1 + 0 = \frac{n(n - 1)}{2}$$

Expanding this gives:
$$\frac{1}{2}n^2 - \frac{1}{2}n$$

In Big-O notation, we drop lower-order terms ($- \frac{1}{2}n$) and constant factors ($\frac{1}{2}$), yielding $O(n^2)$.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(n^2)$
- **Space Complexity**: $O(n^2)$ to store the generated pairs.
