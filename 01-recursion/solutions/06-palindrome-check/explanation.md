# Explanation: 06-palindrome-check

## Two-Pointer Convergence
Instead of slicing `text[1:-1]` (which allocates a new string of size $n - 2$ on every recursive call), two integer indices are used:
- `left` starts at `0` and increases.
- `right` starts at `len(text) - 1` and decreases.

### Base Cases:
1. `left >= right`: All character pairs have matched. Returns `True`.
2. `text[left] != text[right]`: A mismatch is found. Returns `False` immediately (short-circuits without further recursive calls).

## Complexity
- **Time Complexity:**
  - Worst case: $O(n)$ character comparisons when string is a palindrome.
  - Best case: $O(1)$ if the first and last characters differ.
- **Auxiliary Space:** $O(n)$ stack frames in the worst case (depth is $\lfloor n/2 \rfloor$).
