"""
Solution for Drill 10: Deep Nested Dictionary Lookup
Module: 01-recursion
"""


def deep_get(data: dict, keys: list[str], index: int = 0):
    """
    Recursively retrieves a value from a nested dictionary following a list of keys.
    """
    if index == 0 and not isinstance(data, dict):
        raise TypeError("data must be a dict")

    if not keys or index >= len(keys):
        return None

    key = keys[index]

    if not isinstance(data, dict) or key not in data:
        return None

    if index == len(keys) - 1:
        return data[key]

    return deep_get(data[key], keys, index + 1)
