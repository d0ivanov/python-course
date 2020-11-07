import unittest
from unittest_data_provider import data_provider

from snake import Snake
from snake import Game
from snake import Direction


class SnakeTest(unittest.TestCase):

    def setUp(self):
        pass

    def movements():
        return (
            ( Snake([[1, 2], [2, 2], [2, 3]]), Direction.UP, [1, 3] ),
            ( Snake([[1, 2], [2, 2], [2, 3]]), Direction.DOWN, [3, 3] ),
            ( Snake([[1, 2], [2, 2], [2, 3]]), Direction.RIGHT, [2, 4] ),
            ( Snake([[1, 2], [2, 2], [2, 3]]), Direction.LEFT, [2, 2] ),
        )

    @data_provider(movements)
    def test_snake_can_move(self, snake, direction, expected_head):
        snake.move(direction)
        
        self.assertEqual(snake.head, expected_head)

    @data_provider(movements)
    def test_grow(self, snake, direction, expected_head):
        previous_size = len(snake.body)
        snake.grow(direction)

        new_size = len(snake.body)
        self.assertEqual(previous_size + 1, new_size)
        self.assertEqual(snake.head, expected_head)


class GameTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_game(self):
        snake = Snake([[5, 4], [4, 4], [3, 4]])
        game = Game(10, snake, Direction.UP)

        #game.play()


if __name__ == "__main__":
    unittest.main()
