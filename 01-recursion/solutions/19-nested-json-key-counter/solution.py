"""
Solution for Drill 19: Nested JSON Key Counter
Module: 01-recursion
"""


def count_keys(data, target_key: str) -> int:
    """
    Recursively counts occurrences of target_key in arbitrary nested structures.
    """
    total = 0

    if isinstance(data, dict):
        for k, v in data.items():
            if k == target_key:
                total += 1
            total += count_keys(v, target_key)
    elif isinstance(data, list):
        for item in data:
            total += count_keys(item, target_key)

    return total
