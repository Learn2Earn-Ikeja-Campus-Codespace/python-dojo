"""
Solution for Drill 09: Flatten Arbitrarily Nested List
Module: 01-recursion
"""


def flatten(nested: list, index: int = 0) -> list:
    """
    Recursively flattens an arbitrarily nested list of items.
    """
    if not isinstance(nested, list):
        raise TypeError("Input must be a list")

    if index >= len(nested):
        return []

    item = nested[index]
    first_part = flatten(item) if isinstance(item, list) else [item]

    return first_part + flatten(nested, index + 1)
