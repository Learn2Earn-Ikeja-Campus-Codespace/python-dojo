"""
Solution for Drill 01: Countdown Sum of Odd Integers
Module: 01-recursion
"""


def countdown_sum(n: int) -> int:
    """
    Recursively returns the sum of odd positive integers from n down to 1.
    """
    # 1. Type validation: must be an int (excluding bool since bool subclasses int)
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")

    # 2. Base case: if n <= 0, there are no positive odd integers left
    if n <= 0:
        return 0

    # 3. Determine if current n contributes to the sum
    current_value = n if n % 2 != 0 else 0

    # 4. Recursive case: advance strictly towards 0
    return current_value + countdown_sum(n - 1)
