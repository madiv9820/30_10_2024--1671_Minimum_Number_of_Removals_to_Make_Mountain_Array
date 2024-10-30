from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.testCases = {
            1: ([1,3,1], 0),
            2: ([2,1,1,5,6,2,3,1], 3)    
        }
        self.obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        nums, output = self.testCases[1]
        result = self.obj.minimumMountainRemovals(nums = nums)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        nums, output = self.testCases[2]
        result = self.obj.minimumMountainRemovals(nums = nums)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()