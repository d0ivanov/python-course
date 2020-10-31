import subprocess
import sys

from enum import Enum
from getkey import getkey, keys


class Direction(Enum):
    UP = [0, -1]
    DOWN = [0, 1]
    RIGHT = [1, 0]
    LEFT = [-1, 0]

    def __getitem__(self, index):
        return self.value[index]

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



class Game:

    SNAKE_BODY_PART = "*"
    SNAKE_HEAD = "@"
    EMPTY_SPACE = " "

    def __init__(self, size, snake):
        self.size = size
        self.snake = snake
        self.board = []
        for i in range(size):
            columns = []
            for i in range(size):
                columns.append(Game.EMPTY_SPACE)
            self.board.append(columns)

    def play(self):
        while True:
            clear_screen()
            self.__render_board()
            key_press = read_key()
            self.snake.move(self.__get_move_direction(key_press))

    def __render_board(self):
        for i in range(self.size):
            for j in range(self.size):
                symbol = self.board[i][j]
                if self.__is_snake_body_part([i, j]):
                    symbol = Game.SNAKE_BODY_PART
                elif self.__is_snake_head([i, j]):
                    symbol = Game.SNAKE_HEAD
                print("[{}]".format(symbol), end='')
            print()
        print()

    def __get_move_direction(self, key_press):
        return Direction.UP

    def __is_snake_body_part(self, pos):
        return pos in self.snake.body and not self.__is_snake_head(pos)

    def __is_snake_head(self, pos):
        return pos == self.snake.head


if __name__ == "__main__":

    snake = Snake([[5, 4], [4, 4], [3, 4]])
    game = Game(10, snake)
    game.play()











