"""
Unit tests for Drill 15: Queue via Two Stacks
"""
import unittest
from exercise import QueueViaStacks


class TestQueueViaStacks(unittest.TestCase):

    def test_fifo_ordering(self):
        q = QueueViaStacks()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        q.enqueue(4)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertTrue(q.empty())

    def test_empty_errors(self):
        q = QueueViaStacks()
        with self.assertRaises(IndexError):
            q.dequeue()
        with self.assertRaises(IndexError):
            q.peek()


if __name__ == "__main__":
    unittest.main()
