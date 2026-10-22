# Deep-Dive Explanation: 19-subarrays-with-k-sum

## 💡 Algorithmic Thinking

A brute force check of all subarrays takes $O(n^2)$ time.
Let $\text{sum}(i, j)$ be the subarray sum:
$$\text{sum}(i, j) = \text{prefix}[j] - \text{prefix}[i - 1] = k \implies \text{prefix}[i - 1] = \text{prefix}[j] - k$$

By tracking the frequencies of running prefix sums in a hash table:
1. At each element, compute `running_sum`.
2. Check if `running_sum - k` exists in the hash table. If so, add its occurrence count to `count`.
3. Increment frequency of `running_sum`.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(n)$ single pass.
- **Space Complexity**: $O(n)$ for prefix sum frequency map.
