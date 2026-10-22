"""
Solution for Drill 11: Moving Average
Module: 02-big-o-complexity
"""
from collections import deque


class MovingAverage:
    """Computes moving average over sliding window in O(1) time per element."""

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0.0

    def next(self, val: int) -> float:
        """Adds val to stream and returns current moving average."""
        self.queue.append(val)
        self.window_sum += val
        if len(self.queue) > self.size:
            self.window_sum -= self.queue.popleft()
        return self.window_sum / len(self.queue)
