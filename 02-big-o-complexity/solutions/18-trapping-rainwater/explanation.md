# Deep-Dive Explanation: 18-trapping-rainwater

## 💡 Algorithmic Thinking

Water trapped above index $i$ is determined by:
$$\min(\text{max\_left}, \text{max\_right}) - \text{height}[i]$$

Using two pointers converging inward:
- If `height[left] < height[right]`, the bottleneck on the left is guaranteed to be bounded by `height[right]`.
- Thus, water trapped at `left` depends solely on `left_max`.
- Symmetrically, if `height[right] <= height[left]`, water at `right` depends solely on `right_max`.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(n)$ single pass.
- **Space Complexity**: $O(1)$ auxiliary space.
