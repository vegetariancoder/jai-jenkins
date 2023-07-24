"""
This module will test running sum
"""
import unittest
from running_sum import running_sum


class TestMain(unittest.TestCase):
    """
    This is test running_sum
    """

    def __init__(self, nums):
        super().__init__()
        self.nums = nums

    def test_running_sum(self):
        """

        :return: assertion
        """
        self.nums = [1,2,3,4]
        self.assertEqual(running_sum(self.nums),10)
