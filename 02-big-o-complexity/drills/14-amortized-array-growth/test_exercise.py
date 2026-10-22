"""
Unit tests for Drill 14: Amortized Array Growth
"""
import unittest
from exercise import DynamicArraySimulator


class TestAmortizedGrowth(unittest.TestCase):

    def test_resizing_and_copy_counts(self):
        arr = DynamicArraySimulator(initial_capacity=2)
        for i in range(16):
            arr.append(i)
        
        self.assertEqual(arr.size, 16)
        # Cap progression: 2 -> 4 (copy 2) -> 8 (copy 4) -> 16 (copy 8) -> 32 (copy 16)
        self.assertLessEqual(arr.amortized_copy_cost(), 2.0, "Amortized cost must be bounded <= 2.0")


if __name__ == "__main__":
    unittest.main()
