# Explanation: 20-maze-pathfinder

## 2D Grid Backtracking
1. Guard: check out-of-bounds, obstacle (`== 1`), and already-visited.
2. Target match: `start == end`.
3. Add to visited set to prevent infinite loops / cycles.
4. Recurse in 4 cardinal directions.
