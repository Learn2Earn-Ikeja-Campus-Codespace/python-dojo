"""
Solution for Drill 05: Count Target Occurrences
Module: 01-recursion
"""


def count_occurrences(items: list, target, index: int = 0) -> int:
    """
    Recursively counts how many times target appears in items from index forward.
    """
    if not isinstance(items, list):
        raise TypeError("items must be a list")

    # Base case: index reaches the end
    if index >= len(items):
        return 0

    # Contribution of current item
    # Note: in Python, True == 1 and False == 0, so check exact type for booleans
    current = items[index]
    if isinstance(target, bool) or isinstance(current, bool):
        is_match = (current is target)
    else:
        is_match = (current == target)

    match_count = 1 if is_match else 0

    return match_count + count_occurrences(items, target, index + 1)
