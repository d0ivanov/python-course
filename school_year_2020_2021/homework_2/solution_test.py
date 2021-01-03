import unittest

from solution import SimpleCanvas
from solution import Turtle


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.rows = 2
        self.cols = 2
        self.turtle = Turtle(self.rows, self.cols)

    def test_runtime_error_when_turtle_moved_before_spawned(self):
        self.assertRaises(RuntimeError, self.turtle.move)

    def test_spawn_counts_as_visit(self):
        self.turtle.spawn_at(0, 0)

        self.assertGreater(self.turtle.canvas[0][0], 0)
        self.assertEqual(self.turtle.canvas[0][1], 0)
        self.assertEqual(self.turtle.canvas[1][0], 0)
        self.assertEqual(self.turtle.canvas[1][1], 0)

    def test_can_move_once_cell(self):
        self.turtle.spawn_at(1, 0)
        self.turtle.move()

        self.assertEqual(self.turtle.canvas[0][0], 0)
        self.assertEqual(self.turtle.canvas[0][1], 0)
        self.assertGreater(self.turtle.canvas[1][0], 0)
        self.assertGreater(self.turtle.canvas[1][1], 0)

    def test_can_turn_right(self):
        self.turtle.spawn_at(0, 1)
        self.turtle.turn_right()
        self.turtle.move()

        self.assertEqual(self.turtle.canvas[0][0], 0)
        self.assertGreater(self.turtle.canvas[0][1], 0)
        self.assertEqual(self.turtle.canvas[1][0], 0)
        self.assertGreater(self.turtle.canvas[1][1], 0)

    def test_can_turn_left(self):
        self.turtle.spawn_at(1, 1)
        self.turtle.turn_left()
        self.turtle.move()

        self.assertEqual(self.turtle.canvas[0][0], 0)
        self.assertGreater(self.turtle.canvas[0][1], 0)
        self.assertEqual(self.turtle.canvas[1][0], 0)
        self.assertGreater(self.turtle.canvas[1][1], 0)

    def test_moved_to_beginning_of_row_if_end_reached(self):
        self.turtle.spawn_at(0, 0)
        for _ in range(self.cols + 1):
            self.turtle.move()

        expected = [[2, 2],
                    [0, 0]]
        self.assertGreater(self.turtle.canvas[0][0], 0)
        self.assertGreater(self.turtle.canvas[0][1], 0)
        self.assertEqual(self.turtle.canvas[1][0], 0)
        self.assertEqual(self.turtle.canvas[1][1], 0)

    def test_moved_to_beginning_of_column_if_end_reached(self):
        self.turtle.spawn_at(0, 0)
        self.turtle.turn_right()
        for _ in range(self.rows + 1):
            self.turtle.move()

        expected = [[2, 0],
                    [2, 0]]

        self.assertGreater(self.turtle.canvas[0][0], 0)
        self.assertEqual(self.turtle.canvas[0][1], 0)
        self.assertGreater(self.turtle.canvas[1][0], 0)
        self.assertEqual(self.turtle.canvas[1][1], 0)

    def test_canvas_keeps_count_when_we_pass_cell(self):
        self.turtle.spawn_at(0, 0)
        self.turtle.move()

        self.assertEqual(self.turtle.canvas[0][0], 1)
        self.assertEqual(self.turtle.canvas[0][1], 1)
        self.assertEqual(self.turtle.canvas[1][0], 0)
        self.assertEqual(self.turtle.canvas[1][1], 0)

    def test_orientation_kept_after_passing_through_row(self):
        self.turtle.spawn_at(0, 0)
        self.turtle.turn_right()
        self.turtle.move()
        self.turtle.turn_left()
        self.turtle.move()
        self.turtle.move()
        self.turtle.turn_left()
        self.turtle.move()

        self.assertGreater(self.turtle.canvas[0][0], 0)
        self.assertEqual(self.turtle.canvas[0][1], 0)
        self.assertGreater(self.turtle.canvas[1][0], 0)
        self.assertGreater(self.turtle.canvas[1][1], 0)

    def test_orientation_kept_after_passing_through_column(self):
        self.turtle.spawn_at(0, 0)
        self.turtle.turn_left()
        self.turtle.move()
        self.turtle.turn_right()
        self.turtle.move()

        self.assertGreater(self.turtle.canvas[0][0], 0)
        self.assertEqual(self.turtle.canvas[0][1], 0)
        self.assertGreater(self.turtle.canvas[1][0], 0)
        self.assertGreater(self.turtle.canvas[1][1], 0)

    def test_draw_simple_canvas(self):
        result = SimpleCanvas([[1, 0], [0, 0]], ["$", "*"]).draw()
        self.assertEqual(result, "*$\n$$")

    def test_draw_canvas_no_max_visits(self):
        result = SimpleCanvas([[1, 1], [1, 1]], ["$", "*", "#"]).draw()
        self.assertEqual(result, "##\n##")

    def test_draw_canvas(self):
        result = SimpleCanvas(
            [[1, 2], [3, 4]], ["$", "*", "#", "@"]).draw()
        self.assertEqual(result, "*#\n@@")


if __name__ == "__main__":
    unittest.main()
