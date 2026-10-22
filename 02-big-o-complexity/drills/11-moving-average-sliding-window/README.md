# Drill 11: Moving Average via Sliding Window

## Learning Target
Learn to maintain a moving window state in $O(1)$ time per step by adding incoming items and subtracting outgoing items, instead of re-summing $k$ items at $O(k)$ cost.

---

## Problem Statement

Implement `MovingAverage`:
- `__init__(size: int)`: Initializes window with maximum capacity `size`.
- `next(val: int | float) -> float`: Adds `val` to the stream and returns the average of the last `size` values in $O(1)$ time.

---

## Examples

```python
ma = MovingAverage(3)
ma.next(1)  # 1.0 (1 / 1)
ma.next(10) # 5.5 ((1 + 10) / 2)
ma.next(3)  # 4.666... ((1 + 10 + 3) / 3)
ma.next(5)  # 6.0 ((10 + 3 + 5) / 3)
```
