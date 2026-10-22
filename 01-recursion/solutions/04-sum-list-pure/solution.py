"""
Solution for Drill 04: Pure Recursive List Sum
Module: 01-recursion
"""


def sum_list(numbers: list[int | float], index: int = 0) -> int | float:
    """
    Recursively sums elements of numbers from index to len(numbers) - 1.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    # Base case: if index reaches the end of the list
    if index >= len(numbers):
        return 0

    # Recursive step: current element + sum of remaining elements
    return numbers[index] + sum_list(numbers, index + 1)
