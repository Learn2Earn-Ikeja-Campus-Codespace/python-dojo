# Deep-Dive Explanation: 01-countdown-sum

## 🧠 Algorithmic Thinking

### 1. Base Case Identification
When calculating sums recursively from $n$ down to $1$, the stopping condition occurs when $n$ is no longer positive ($n \le 0$). At that point, the answer is trivially $0$.

### 2. Recursive Progression
At each step, we look at the current value of $n$:
- If $n$ is odd (`n % 2 != 0`), it contributes its value $n$.
- If $n$ is even (`n % 2 == 0`), it contributes $0$.

We then add that contribution to the result of `countdown_sum(n - 1)`. Because $n$ decreases by $1$ on every call, we are guaranteed to reach the base case in finite steps.

---

## ⚡ Complexity Analysis

- **Time Complexity**: $O(n)$
  There are $n + 1$ recursive calls, each performing $O(1)$ operations (modulo, addition, comparison).
- **Space (Memory) Complexity**: $O(n)$
  Python does not optimize tail calls. Each call creates an active frame on the call stack until $n = 0$ is reached. For $n = 5$, there are 6 stack frames alive simultaneously.

---

## ⚠️ Python Edge Case: `bool` is an `int`
In Python:
```python
isinstance(True, int)  # Returns True!
```
Because `bool` inherits from `int` in Python (`True == 1`, `False == 0`), strict type-checking must explicitly guard against booleans:
```python
if not isinstance(n, int) or isinstance(n, bool):
    raise TypeError(...)
```
