# Deep-Dive Explanation: 14-amortized-array-growth

## 💡 Algorithmic Thinking

A single resize operation costs $O(n)$ because it copies all $n$ existing elements to a newly allocated contiguous block of memory.
However, because capacity doubles each time:
$$\text{Total copies} = 1 + 2 + 4 + 8 + \dots + \frac{n}{2} < n$$

Dividing total copy operations by $n$ total appends gives:
$$\frac{\text{Total copies}}{n} < \frac{n}{n} = 1$$

Therefore, the amortized cost per append is $O(1)$.

---

## 📊 Complexity Analysis

- **Worst-Case Single Append**: $O(n)$ when resizing occurs.
- **Amortized Append Cost**: $O(1)$ constant average.
