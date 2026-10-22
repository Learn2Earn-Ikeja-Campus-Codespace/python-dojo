# Deep-Dive Explanation: 12-matrix-search-elimination

## 💡 Algorithmic Thinking

In a matrix where each row and column is sorted in ascending order:
- Starting at the **top-right corner** `(0, cols - 1)`:
  - If current value $>$ target, every element below it in that column is also $>$ target, so decrement column pointer `c -= 1`.
  - If current value $<$ target, every element to its left in that row is also $<$ target, so increment row pointer `r += 1`.
Each step eliminates an entire row or column.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(m + n)$
- **Space Complexity**: $O(1)$ auxiliary space.
