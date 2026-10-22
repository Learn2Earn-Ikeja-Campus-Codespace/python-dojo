# Explanation: 17-coin-change-count

## Unbounded Knapsack Tree
At each state `(amount, coin_index)`:
1. `take`: Subtract `coins[coin_index]` from amount, remain at `coin_index`.
2. `skip`: Leave amount unchanged, advance to `coin_index + 1`.
