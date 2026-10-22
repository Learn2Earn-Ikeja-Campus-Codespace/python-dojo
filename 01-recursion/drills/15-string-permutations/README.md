# Drill 15: String Permutations

## Learning Target
Learn backtracking with state swapping/rebuilding to generate all $n!$ orderings of a string.

---

## Problem Statement

Write a function `permutations(text: str) -> list[str]` that recursively returns all unique permutations of characters in `text`.

### Rules & Constraints:
1. Do not use `itertools.permutations`.
2. Base case: empty string returns `[""]`, 1-character string returns `[text]`.
3. If input is not a string, raise `TypeError`.

---

## Examples

```python
permutations("ab")   # ["ab", "ba"]
permutations("abc")  # ["abc", "acb", "bac", "bca", "cab", "cba"]
permutations("")     # [""]
```
