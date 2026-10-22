"""
Solution for Drill 12: Matrix Search Elimination
Module: 02-big-o-complexity
"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Searches row- and column-sorted matrix in O(m + n) time and O(1) space."""
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    r = 0
    c = cols - 1

    while r < rows and c >= 0:
        val = matrix[r][c]
        if val == target:
            return True
        elif val > target:
            c -= 1  # Target cannot be in this column
        else:
            r += 1  # Target cannot be in this row

    return False
