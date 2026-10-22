# Explanation: 13-pascal-triangle-cell

## 2D State Recurrence
Each interior cell is the sum of the two cells directly above it. Using a coordinate tuple `(row, col)` as the memo key avoids overlapping subproblem recalculation.
