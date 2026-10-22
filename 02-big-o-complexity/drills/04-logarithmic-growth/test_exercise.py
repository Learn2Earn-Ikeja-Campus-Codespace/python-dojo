"""
Unit tests for Drill 04: Logarithmic Growth
"""
import unittest
from exercise import count_divisions


class TestLogarithmicGrowth(unittest.TestCase):

    def test_powers_of_two(self):
        self.assertEqual(count_divisions(1), 0)
        self.assertEqual(count_divisions(2), 1)
        self.assertEqual(count_divisions(4), 2)
        self.assertEqual(count_divisions(8), 3)
        self.assertEqual(count_divisions(16), 4)
        self.assertEqual(count_divisions(1024), 10)

    def test_non_powers_of_two(self):
        self.assertEqual(count_divisions(9), 3) # 9 -> 4 -> 2 -> 1
        self.assertEqual(count_divisions(15), 3)
        self.assertEqual(count_divisions(100), 6)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            count_divisions(0)
        with self.assertRaises(ValueError):
            count_divisions(-5)


if __name__ == "__main__":
    unittest.main()
