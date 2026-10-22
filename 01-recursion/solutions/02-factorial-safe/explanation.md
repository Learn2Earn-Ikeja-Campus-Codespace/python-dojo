# Explanation: 02-factorial-safe

## Mathematical Basis
By convention in mathematics, the empty product is 1, so $0! = 1$. This is essential because it maintains the recurrence relation:
$$n! = \frac{(n + 1)!}{n + 1}$$
Setting $n = 0$ gives $0! = \frac{1!}{1} = 1$.

## Implementation Notes
1. **Type Checking:** In Python, `isinstance(True, int)` evaluates to `True`. Because factorial is not meaningful for booleans, checking `isinstance(n, bool)` prevents subtle bugs where `factorial(True)` would return `1`.
2. **Domain Checking:** Negative numbers do not terminate if decremented by 1, leading to `RecursionError` unless explicitly guarded.
3. **Complexity:**
   - Time: $O(n)$ operations.
   - Auxiliary Space: $O(n)$ stack frames.
