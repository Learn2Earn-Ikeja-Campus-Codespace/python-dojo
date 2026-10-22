# Explanation: 07-fibonacci-memo

## Why Memoization Transforms $O(2^n) \to O(n)$
Without memoization, the recursive call tree recalculates the exact same subproblems repeatedly:
`fib(5)` calls `fib(4)` and `fib(3)`. `fib(4)` also calls `fib(3)` and `fib(2)`. The number of calls doubles at each level, producing exponential $O(2^n)$ work.

By storing computed results in a `memo` dictionary:
- Each value from $0$ to $n$ is calculated exactly **once**.
- Subsequent requests for `fib(k)` return in $O(1)$ dictionary lookup time.
- Total time complexity drops to $O(n)$.
- Auxiliary space is $O(n)$ ($n$ stack frames + $n$ entries in dictionary).
