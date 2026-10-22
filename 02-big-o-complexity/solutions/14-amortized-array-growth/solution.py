"""
Solution for Drill 14: Dynamic Array Amortized Analysis
Module: 02-big-o-complexity
"""


class DynamicArraySimulator:
    """Simulates dynamic array doubling and tracks resizing cost."""

    def __init__(self, initial_capacity: int = 2):
        self.capacity = initial_capacity
        self.size = 0
        self.copy_operations = 0
        self.total_appends = 0

    def append(self, value):
        """Appends value, doubling capacity and copying when full."""
        self.total_appends += 1
        if self.size == self.capacity:
            self.copy_operations += self.size
            self.capacity *= 2
        self.size += 1

    def amortized_copy_cost(self) -> float:
        """Returns average copy operations per append."""
        if self.total_appends == 0:
            return 0.0
        return self.copy_operations / self.total_appends
