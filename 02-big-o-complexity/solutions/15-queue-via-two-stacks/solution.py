"""
Solution for Drill 15: Queue via Two Stacks
Module: 02-big-o-complexity
"""


class QueueViaStacks:
    """Implements FIFO Queue using two LIFO Stacks with amortized O(1) dequeue."""

    def __init__(self):
        self._in_stack = []
        self._out_stack = []

    def enqueue(self, val):
        """Pushes element to in-stack in O(1)."""
        self._in_stack.append(val)

    def _shift(self):
        """Moves elements from in_stack to out_stack if out_stack is empty."""
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

    def dequeue(self):
        """Pops FIFO front element with amortized O(1) runtime."""
        self._shift()
        if not self._out_stack:
            raise IndexError("Dequeue from empty queue")
        return self._out_stack.pop()

    def peek(self):
        """Returns front element without removing it."""
        self._shift()
        if not self._out_stack:
            raise IndexError("Peek from empty queue")
        return self._out_stack[-1]

    def empty(self) -> bool:
        """Returns True if queue contains no elements."""
        return len(self._in_stack) == 0 and len(self._out_stack) == 0
