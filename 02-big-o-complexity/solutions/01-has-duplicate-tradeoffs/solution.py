"""
Solution for Drill 01: Duplicate Detection & The 3 Classical Trade-offs
Module: 02-big-o-complexity
"""


def has_duplicate_quadratic(items: list) -> bool:
    """Checks for duplicates in O(n^2) time and O(1) space."""
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            if items[i] == items[j]:
                return True
    return False


def has_duplicate_hash(items: list) -> bool:
    """Checks for duplicates in expected O(n) time and O(n) space."""
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False


def has_duplicate_sorted(items: list) -> bool:
    """Checks for duplicates in O(n log n) time using sorting and adjacent comparison."""
    if len(items) < 2:
        return False
    sorted_items = sorted(items)
    for i in range(len(sorted_items) - 1):
        if sorted_items[i] == sorted_items[i + 1]:
            return True
    return False
