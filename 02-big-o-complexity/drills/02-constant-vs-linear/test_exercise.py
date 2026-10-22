"""
Unit tests for Drill 02: Constant vs Linear
"""
import unittest
from exercise import get_extremes_constant, get_extremes_linear


class TestConstantVsLinear(unittest.TestCase):

    def test_standard_lists(self):
        self.assertEqual(get_extremes_constant([1, 2, 3]), (1, 3))
        self.assertEqual(get_extremes_linear([1, 2, 3]), (1, 3))
        self.assertEqual(get_extremes_constant(["a"]), ("a", "a"))
        self.assertEqual(get_extremes_linear(["a"]), ("a", "a"))

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            get_extremes_constant([])
        with self.assertRaises(ValueError):
            get_extremes_linear([])


if __name__ == "__main__":
    unittest.main()
