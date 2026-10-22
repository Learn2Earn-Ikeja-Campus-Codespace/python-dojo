"""
Solution for Drill 08: Array Intersection
Module: 02-big-o-complexity
"""


def intersection(a: list, b: list) -> list:
    """Computes unique common elements in O(n + m) time using hash set lookups."""
    set_b = set(b)
    seen = set()
    result = []
    for item in a:
        if item in set_b and item not in seen:
            seen.add(item)
            result.append(item)
    return result
