# Deep-Dive Explanation: 07-two-sum-tradeoffs

## 💡 Algorithmic Thinking

Instead of comparing all $O(n^2)$ pairs, we take advantage of the algebraic relation:
$$\text{complement} = \text{target} - \text{num}$$

By mapping each visited number to its index in a hash map, looking up whether the complement has already been seen takes $O(1)$ expected time. A single pass yields the answer.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(n)$ single pass with $O(1)$ average hash lookups.
- **Space Complexity**: $O(n)$ to store up to $n$ entries in the dictionary.
