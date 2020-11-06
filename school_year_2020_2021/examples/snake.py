import subprocess
import sys
import random

from enum import Enum
from getkey import getkey, keys


class Direction(Enum):
    UP    = (-1, 0)
    DOWN  = (1, 0)
    RIGHT = (0, 1)
    LEFT  = (0, -1)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, index):
        return self.value[index]

    def is_opposite_of(self, other):
        return self.x == (-1 * other.x) and self.y == (-1 * other.y)


def clear_screen():
    subprocess.call('clear',shell=True)


def read_key(valid_keys = [keys.UP, keys.LEFT, keys.RIGHT, keys.DOWN]):
    key = getkey()
    while key not in valid_keys:
        key = getkey()
    return key


class Snake:

    def __init__(self, initial_body):
        self.body = initial_body

    @property
    def head(self):
        return self.body[-1]

    def move(self, direction):
        new_head = [self.head[0] + direction[0], self.head[1] + direction[1]]
        self.body.append(new_head)
        self.body = self.body[1:]

    def grow(self, direction):
        pass

class Game:

    SNAKE_BODY_PART = "*"
    SNAKE_HEAD = "@"
    FOOD = "+"
    EMPTY_SPACE = " "

    def __init__(self, size, snake):
        self.size = size
        self.snake = snake
        self.board = []
        self.food = self.__new_food()
        for i in range(size):
            columns = []
            for i in range(size):
                columns.append(Game.EMPTY_SPACE)
            self.board.append(columns)

    def play(self):
        # TODO: Fix me - calculate current direction based on head coords
        current_direction = Direction.UP
        while True:
            clear_screen()
            self.__render_board()
            key_press = read_key()
            next_direction = self.__get_move_direction(key_press)
            if next_direction.is_opposite_of(current_direction):
                continue
            current_direction = next_direction
            self.snake.move(next_direction)
            if self.food == self.snake.head:
                self.snake.grow(current_direction)
                self.food = self.__new_food()
            if self.__is_outside_of_board():
                break

        print("Game over!")

    def __render_board(self):
        for i in range(self.size):
            for j in range(self.size):
                symbol = self.board[i][j]
                if self.__is_snake_body_part([i, j]):
                    symbol = Game.SNAKE_BODY_PART
                elif self.__is_snake_head([i, j]):
                    symbol = Game.SNAKE_HEAD
                elif self.__is_food([i, j]):
                    symbol = Game.FOOD
                print("[{}]".format(symbol), end='')
            print()
        print()

    def __get_move_direction(self, key_press):
        if key_press == keys.UP:
            return Direction.UP
        elif key_press == keys.DOWN:
            return Direction.DOWN
        elif key_press == keys.LEFT:
            return Direction.LEFT
        elif key_press == keys.RIGHT:
            return Direction.RIGHT

    def __new_food(self):
        cells = []
        for i in range(self.size):
            for j in range(self.size):
                if [i, j] not in self.snake.body:
                   cells.append([i, j])
        return random.choice(cells)


    def __is_outside_of_board(self):
        head = self.snake.head
        return (head[0] < 0 or head[0] > self.size - 1) or \
                    (head[1] < 0 or head[1] > self.size - 1)

    def __is_snake_body_part(self, pos):
        return pos in self.snake.body and not self.__is_snake_head(pos)

    def __is_snake_head(self, pos):
        return pos == self.snake.head
    
    def __is_food(self, pos):
        return pos == self.food


if __name__ == "__main__":

    snake = Snake([[5, 4], [4, 4], [3, 4]])
    game = Game(10, snake)
    game.play()











