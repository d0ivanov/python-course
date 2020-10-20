import unittest
import solution


class SolutionTest(unittest.TestCase):

    def test_accumulate_left(self):
        res = solution.accumulate_left(lambda a, b: a / b, 64, [2, 4, 8])
        self.assertEqual(1.0, res)

    def test_accumulate_left_over_tuple(self):
        res = solution.accumulate_left(lambda a, b: a / b, 64, (2, 4, 8))
        self.assertEqual(1.0, res)

    def test_accumulate_left_list(self):
        res = solution.accumulate_left(
                lambda a, b: a + b, [], [[1, 2, 3], [4, 5, 6]])
        self.assertEqual([1, 2, 3, 4, 5, 6], res)

    def test_accumulate_left_over_empty_list(self):
        res = solution.accumulate_left(lambda a, b: a / b, 8, [])
        self.assertEqual(8, res)

    def test_accumulate_left_over_empty_tuple(self):
        res = solution.accumulate_left(lambda a, b: a / b, 8, ())
        self.assertEqual(8, res)

    def test_accumulate_right(self):
        res = solution.accumulate_right(lambda a, b: a / b, 8, [16, 32, 64])
        self.assertEqual(4.0, res)

    def test_accumulate_right_over_tuple(self):
        res = solution.accumulate_right(lambda a, b: a / b, 8, (16, 32, 64))
        self.assertEqual(4.0, res)

    def test_accumulate_right_list(self):
        res = solution.accumulate_right(lambda a, b: a + b, [], [[1, 2], [3, 4]])
        self.assertEqual([1, 2, 3, 4], res)

    def test_accumulate_right_over_empty_list(self):
        res = solution.accumulate_right(lambda a, b: a / b, 8, [])
        self.assertEqual(8, res)

    def test_accumulate_righ_over_empty_tuple(self):
        res = solution.accumulate_right(lambda a, b: a / b, 8, ())
        self.assertEqual(8, res)


if __name__ == "__main__":
    unittest.main()
