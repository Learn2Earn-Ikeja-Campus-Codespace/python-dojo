# Deep-Dive Explanation: 17-product-except-self

## 💡 Algorithmic Thinking

The product of all elements except `nums[i]` is:
$$\text{product} = (\text{product of elements before } i) \times (\text{product of elements after } i)$$

1. First pass (left to right): Compute prefix product up to $i - 1$ and store it in `res[i]`.
2. Second pass (right to left): Maintain a running `suffix` product and multiply it into `res[i]`.
Zero division is avoided completely.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(n)$ with two linear passes.
- **Space Complexity**: $O(1)$ auxiliary space (excluding output array).
