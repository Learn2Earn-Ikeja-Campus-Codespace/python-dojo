# Drill 20: 2D Grid Maze Pathfinder (Backtracking)

## Learning Target
Master 2D grid backtracking with visited state exploration and pruning.

---

## Problem Statement

Write a function `has_path(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int], visited: set | None = None) -> bool` that determines if a valid path exists from `start` to `end`.

- `grid[r][c] == 0`: Open cell.
- `grid[r][c] == 1`: Obstacle/Wall (cannot pass).
- Movements allowed: Up, Down, Left, Right (4-directional).

### Rules & Constraints:
1. Returns `True` if `start == end` and cell is open.
2. Never visits the same cell twice along the current path.
3. Bounds check: out-of-grid cells cannot be traversed.

---

## Examples

```python
maze = [
    [0, 0, 1],
    [1, 0, 1],
    [1, 0, 0]
]

has_path(maze, (0, 0), (2, 2))  # True
has_path(maze, (0, 0), (0, 2))  # False (blocked by wall)
```
