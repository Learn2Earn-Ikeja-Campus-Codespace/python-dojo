"""
Unit tests for Drill 03: Dependent Nested Loop Counting
"""
import unittest
from exercise import count_unique_pairs


class TestDependentLoops(unittest.TestCase):

    def test_pair_count_and_operations(self):
        items = ["a", "b", "c", "d", "e"] # n = 5
        pairs, count = count_unique_pairs(items)
        # Formula: n*(n-1)/2 = 5*4/2 = 10
        self.assertEqual(len(pairs), 10)
        self.assertEqual(count, 10)

    def test_small_lists(self):
        pairs, count = count_unique_pairs([1])
        self.assertEqual(pairs, [])
        self.assertEqual(count, 0)

        pairs, count = count_unique_pairs([1, 2])
        self.assertEqual(pairs, [(1, 2)])
        self.assertEqual(count, 1)


if __name__ == "__main__":
    unittest.main()
