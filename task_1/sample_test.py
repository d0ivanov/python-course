import unittest
import solution


class SolutionTest(unittest.TestCase):

    def test_accumulate_left(self):
        res = solution.accumulate_left(lambda a, b: a / b, 64, [2, 4, 8])
        self.assertEqual(1.0, res)

    def test_accumulate_right(self):
        res = solution.accumulate_right(lambda a, b: a / b, [8, 12, 24, 4], 2)
        self.assertEqual(4.0, res)


if __name__ == "__main__":
    unittest.main()
