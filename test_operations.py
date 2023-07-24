"""
This module is to test running sum
"""
import unittest
from running_sum import running_sum


class TestMain(unittest.TestCase):
    """
    This is test running_sum
    """

    def test_running_sum_with_valid_input(self):
        """
        Test running_sum with a valid input list.
        """
        nums = [1, 2, 3, 4]
        self.assertEqual(running_sum(nums), 10)

    def test_running_sum_with_empty_list(self):
        """
        Test running_sum with an empty input list.
        """
        nums = []
        self.assertEqual(running_sum(nums), 0)

    def test_running_sum_with_non_list_input(self):
        """
        Test running_sum with a non-list input.
        """
        nums = 10
        self.assertEqual(running_sum(nums), "Please enter the list for input")


if __name__ == '__main__':
    unittest.main()
