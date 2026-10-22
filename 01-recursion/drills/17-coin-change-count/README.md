# Drill 17: Coin Change Combinations Count

## Learning Target
Learn the classic unbounded knapsack decision tree: at each step, either use the current coin or move to the next denomination.

---

## Problem Statement

Write a function `coin_change_ways(amount: int, coins: list[int], coin_index: int = 0, memo: dict | None = None) -> int` that returns the number of distinct ways to make change for `amount` using the available `coins`.

### Rules & Constraints:
1. Unlimited quantity of each coin is available.
2. If `amount == 0`, return `1`.
3. If `amount < 0` or no coins remain, return `0`.
4. Use memoization with key `(amount, coin_index)`.

---

## Examples

```python
coin_change_ways(4, [1, 2])     # 3: [1+1+1+1, 1+1+2, 2+2]
coin_change_ways(5, [1, 2, 5])  # 4: [1*5, 1*3+2, 1+2*2, 5]
coin_change_ways(3, [2])        # 0
```
