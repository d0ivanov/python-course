import unittest

from solution import SimpleCanvas
from solution import Turtle


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.turtle = Turtle(3, 3)
        self.turtle.spawn_at(0, 0)

    def test_turtle_can_move(self):
        self.turtle.move()
        self.assertEqual([[1, 1,  0], [0, 0 ,0], [0, 0, 0]], self.turtle.canvas)

    def test_turtle_can_turn_right(self):
        self.turtle.turn_right()
        self.turtle.move()
        self.assertEqual([[1, 0,  0], [1, 0 ,0], [0, 0, 0]], self.turtle.canvas)

    def test_turtle_can_turn_left(self):
        self.turtle.turn_left()
        self.turtle.move()
        self.assertEqual([[1, 0,  0], [0, 0 ,0], [1, 0, 0]], self.turtle.canvas)

    def test_canvas_drawn_correctly(self):
        for i in range(9):
            self.turtle.move()
        self.turtle.turn_right()
        for i in range(4):
            self.turtle.move()
        self.turtle.turn_left()
        self.turtle.move()
        self.turtle.move()
        self.turtle.turn_right()
        self.turtle.move()
        canvas = SimpleCanvas(self.turtle.canvas, [' ', '*', '@', '#'])
        canvas.draw()

        self.assertEqual("#@@\n@**\n* *", canvas.draw())


if __name__ == "__main__":
    unittest.main()
