"""
Solution for Drill 03: Dependent Nested Loop Counting
Module: 02-big-o-complexity
"""


def count_unique_pairs(items: list) -> tuple[list[tuple], int]:
    """Generates all unique index-ordered pairs and returns (pairs, comparisons_count)."""
    pairs = []
    comparisons = 0
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((items[i], items[j]))
            comparisons += 1
    return pairs, comparisons
