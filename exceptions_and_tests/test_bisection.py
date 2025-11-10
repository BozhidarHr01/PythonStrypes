import unittest
from bisection import InvalidRangeException, bisection, func

class TestCorrectValuesForAandB(unittest.TestCase):
    def runTest(self):
        f = lambda x: func(x)
        expected_root = 1.154296
        root = bisection(f(1), f(2), 0.001)

        self.assertAlmostEqual(root, expected_root, places=3, msg=f"Expected {expected_root}, actual: {root}")

class TestInvalidRange(unittest.TestCase):
    def runTest(self):
        self.assertRaises(InvalidRangeException, bisection, 1, 1, 0.001)

class TestInvalidValuesForAandB(unittest.TestCase):
    def runTest(self):
        self.assertRaises(TypeError, bisection, 1, 'a', 0.001)
        self.assertRaises(TypeError, bisection, 'a', 1, 0.001)
        self.assertRaises(TypeError, bisection, 1, 2, 'a')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCorrectValuesForAandB())
    suite.addTest(TestInvalidRange())
    suite.addTest(TestInvalidValuesForAandB())
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)