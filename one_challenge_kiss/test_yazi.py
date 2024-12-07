import unittest
from yazi import count_fruits  # Import the function from yazi.py

class TestYazi(unittest.TestCase):
    def test_count_fruits(self):
        fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
        result = count_fruits(fruits)
        expected = {"apple": 3, "banana": 2, "orange": 1}
        self.assertEqual(result, expected)

    def test_empty_list(self):
        fruits = []
        result = count_fruits(fruits)
        expected = {}
        self.assertEqual(result, expected)

    def test_single_fruit(self):
        fruits = ["apple"]
        result = count_fruits(fruits)
        expected = {"apple": 1}
        self.assertEqual(result, expected)

# Entry point to run the tests
if __name__ == "__main__":
    unittest.main()
