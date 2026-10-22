# Deep-Dive Explanation: 20-empirical-growth-benchmark

## 💡 Algorithmic Thinking

Big-O complexity describes asymptotic rate of growth:
- Linear $O(n)$: Doubling input size $n_2 = 2n_1$ doubles execution time: $\frac{T(2n)}{T(n)} \approx 2$.
- Quadratic $O(n^2)$: Doubling input size quadruples execution time: $\frac{T(2n)}{T(n)} \approx 4$.
- Logarithmic $O(\log n)$: Doubling input size adds a constant increment: $\frac{T(2n)}{T(n)} \approx 1$.

Empirical benchmarking requires pre-allocating test inputs outside timing windows and running multiple repetitions to mitigate OS context switches and cache jitter.

---

## 📊 Complexity Analysis

- **Time Complexity**: Proportional to $O(fn(n_1) + fn(n_2))$.
- **Space Complexity**: $O(n_1 + n_2)$ for input lists.
