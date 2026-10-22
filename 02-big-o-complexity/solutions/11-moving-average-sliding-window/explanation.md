# Deep-Dive Explanation: 11-moving-average-sliding-window

## 💡 Algorithmic Thinking

Recalculating the average by summing all $k$ items in the window requires $O(k)$ time per step.
With a sliding window:
1. Add the incoming value to `window_sum`.
2. When the window exceeds `size`, pop the oldest element from the queue and subtract it from `window_sum`.
3. Division by the window size yields the new average in constant time.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ per `next()` invocation.
- **Space Complexity**: $O(k)$ where $k$ is the window size.
