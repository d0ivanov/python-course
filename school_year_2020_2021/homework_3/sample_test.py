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
        gen = solution.simulation(self.grid)
        gen0 = next(gen)
        gen1 = next(gen)
        expected = [[0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
        self.assertEqual(expected, gen0)
        self.assertEqual(expected, gen1)

    def test_lonely_death(self):
        self.grid[2][2] = 1
        gen = solution.simulation(self.grid)
        gen0 = next(gen)
        gen1 = next(gen)
        expected = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
        self.assertEqual(expected, gen0)
        expected[2][2] = 0
        self.assertEqual(expected, gen1)


if __name__ == "__main__":
    unittest.main()
