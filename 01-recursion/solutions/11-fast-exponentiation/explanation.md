# Explanation: 11-fast-exponentiation

## Binary Exponentiation
Instead of multiplying `base` $n$ times ($O(n)$):
- Calculate `half = power(base, exp // 2)`.
- If even: `half * half`.
- If odd: `base * half * half`.
Each step halves `exp`, reducing calls to $O(\log n)$.
