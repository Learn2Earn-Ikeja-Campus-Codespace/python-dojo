# Deep-Dive Explanation: 02-constant-vs-linear

## 💡 Algorithmic Thinking

### 1. Constant Time ($O(1)$)
Python lists are contiguous arrays of object pointers. Indexing `nums[0]` and `nums[-1]` performs pointer arithmetic directly in memory, executing in identical time regardless of whether the list contains 10 elements or 10,000,000 elements.

### 2. Linear Time ($O(n)$)
Iterating through a list visits every single element sequentially. Even though we only need the first and last elements, full traversal forces the CPU to make $n$ loop cycles.

---

## 📊 Complexity Analysis

- **`get_extremes_constant`**: $O(1)$ time, $O(1)$ space.
- **`get_extremes_linear`**: $O(n)$ time, $O(1)$ space.
