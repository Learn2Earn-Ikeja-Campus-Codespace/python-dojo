"""
Solution for Drill 20: 2D Grid Maze Pathfinder
Module: 01-recursion
"""


def has_path(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int], visited: set | None = None) -> bool:
    """
    Determines if path exists from start to end in 2D grid.
    """
    if not grid or not grid[0]:
        return False

    r, c = start
    rows, cols = len(grid), len(grid[0])

    # Bounds check
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False

    # Obstacle check
    if grid[r][c] == 1:
        return False

    if visited is None:
        visited = set()

    if start in visited:
        return False

    if start == end:
        return True

    visited.add(start)

    # Explore 4 directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        next_pos = (r + dr, c + dc)
        if has_path(grid, next_pos, end, visited):
            return True

    return False
