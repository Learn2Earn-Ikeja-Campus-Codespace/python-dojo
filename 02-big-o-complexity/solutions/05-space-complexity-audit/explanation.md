# Deep-Dive Explanation: 05-space-complexity-audit

## 💡 Algorithmic Thinking

### 1. In-Place Invariant ($O(1)$ Space)
Using two pointers (`left` and `right`), we swap opposite elements and march toward the center until `left >= right`. Only a couple of integer variables are held in memory.

### 2. Allocation Variant ($O(n)$ Space)
Creating a new list allocates a new block of memory proportional to $n$. While convenient, it doubles peak memory consumption.

---

## 📊 Complexity Analysis

- **`reverse_with_allocation`**: $O(n)$ time, $O(n)$ auxiliary space.
- **`reverse_in_place`**: $O(n)$ time, $O(1)$ auxiliary space.
