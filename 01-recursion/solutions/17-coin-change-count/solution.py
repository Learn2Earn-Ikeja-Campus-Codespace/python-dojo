"""
Solution for Drill 17: Coin Change Combinations Count
Module: 01-recursion
"""


def coin_change_ways(amount: int, coins: list[int], coin_index: int = 0, memo: dict | None = None) -> int:
    """
    Counts ways to make change using unbounded coins.
    """
    if amount == 0:
        return 1
    if amount < 0 or coin_index >= len(coins):
        return 0

    if memo is None:
        memo = {}

    key = (amount, coin_index)
    if key in memo:
        return memo[key]

    # Choice 1: Take current coin (stay at coin_index since unbounded)
    take = coin_change_ways(amount - coins[coin_index], coins, coin_index, memo)
    # Choice 2: Skip current coin and move to next
    skip = coin_change_ways(amount, coins, coin_index + 1, memo)

    memo[key] = take + skip
    return memo[key]
