import unittest
import solution


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.grid = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
        ]

    def test_block(self):
        self.grid[1][1] = 1
        self.grid[1][2] = 1
        self.grid[2][1] = 1
        self.grid[2][2] = 1
        result = solution.next_generation(self.grid)
        expected = [[0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
        self.assertEqual(expected, result)

    def test_lonely_death(self):
        self.grid[2][2] = 1
        result = solution.next_generation(self.grid)
        expected = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
