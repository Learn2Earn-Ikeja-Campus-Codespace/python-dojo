# Explanation: 16-climbing-stairs

## 3-Way Recurrence
To land on step $n$, you must come from step $n-1$, $n-2$, or $n-3$:
$$W(n) = W(n-1) + W(n-2) + W(n-3)$$
