# Deep-Dive Explanation: 04-logarithmic-growth

## 💡 Algorithmic Thinking

Repeated halving of an input size is the fundamental hallmark of $O(\log n)$ complexity.
If $n = 2^k$, then dividing by 2 exactly $k$ times reduces $n$ to 1:

$$n = 2^k \implies k = \log_2(n)$$

For inputs that are not powers of two, the number of floor divisions is $\lfloor \log_2(n) \rfloor$.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(\log n)$ iterations.
- **Space Complexity**: $O(1)$ auxiliary space.
