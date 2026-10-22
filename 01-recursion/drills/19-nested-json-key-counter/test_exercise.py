"""
Unit tests for Drill 19: Nested JSON Key Counter
"""
import unittest
from exercise import count_keys


class TestNestedJSONKeyCounter(unittest.TestCase):

    def test_nested_dictionaries_and_lists(self):
        payload = {
            "id": 1,
            "profile": {
                "id": 2,
                "history": [
                    {"id": 3, "action": "login"},
                    {"id": 4, "action": "logout"},
                    "plain string",
                    100
                ]
            }
        }
        self.assertEqual(count_keys(payload, "id"), 4)
        self.assertEqual(count_keys(payload, "action"), 2)
        self.assertEqual(count_keys(payload, "nonexistent"), 0)

    def test_empty_structures(self):
        self.assertEqual(count_keys({}, "a"), 0)
        self.assertEqual(count_keys([], "a"), 0)

    def test_primitive_root(self):
        self.assertEqual(count_keys(42, "a"), 0)
        self.assertEqual(count_keys("hello", "a"), 0)


if __name__ == "__main__":
    unittest.main()
