from running_sum import running_sum
import unittest

class TestMain(unittest.TestCase):

    def test_running_sum(self):
        self.nums = [1,2,3,4]
        self.assertEqual(running_sum(self.nums),10)