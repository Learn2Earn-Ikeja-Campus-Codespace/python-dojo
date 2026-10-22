"""
Drill 17: Coin Change Combinations Count
Module: 01-recursion
"""


def coin_change_ways(amount: int, coins: list[int], coin_index: int = 0, memo: dict | None = None) -> int:
    """
    Recursively counts ways to make change for amount using given coins.

    Args:
        amount (int): Target sum.
        coins (list[int]): Available denominations.
        coin_index (int): Current coin denomination index.
        memo (dict | None): Cache dictionary.

    Returns:
        int: Number of ways.
    """
    # TODO: Implement take/skip decision tree with memoization
    pass
