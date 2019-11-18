import random
import time
import subprocess
import sys

from enum import Enum
from getkey import getkey, keys

# snake - масив с всички последователни позиции, на които е разположена змията,
#         като на последната позиция се намира главата.
# Пример: [[4, 5], [4, 6], [5, 6], [5, 7]]

# direction - масив от две числа (-1, 0 или 1), описващ посоката на движение.
# Първият елемент е промяната по абсцисата (x), а вторият - по ординатата (y).

# Тоест:
#
# [0, 1] - нагоре
# [0, -1] - надолу
# [1, 0] - надясно
# [-1, 0] - наляво

# food - масив с всички позиции, на които има храна за ядене.
#
# Пример: [[3, 2], [1, 1], [0, 5]]

# Позиция на змията

# y ^
#   |                        Легенда:
# 7 | [ ][ ][ ][ ][ ]        * - тяло на змията
# 6 | [ ][ ][ ][ ][ ]        @ - глава на змията
# 5 | [ ][ ][@][X][ ]        X - позиция пред змията
# 4 | [ ][ ][*][ ][ ]
# 3 | [ ][ ][*][ ][ ]
# 2 | [ ][*][*][ ][ ]
# 1 | [ ][*][ ][ ][ ]
# 0 | [ ][ ][ ][ ][ ]
#   ------------------->
#      0  1  2  3  4   x


class Direction(Enum):
    UP = [0, -1]
    DOWN = [0, 1]
    RIGHT = [1, 0]
    LEFT = [-1, 0]

    def __getitem__(self, index):
        return self.value[index]


def cells(width, height):
    cells = []
    for i in range(width):
        for j in range(height):
            cells.append([i, j])
    return cells
    # Или с list comprehension
    #return [ [i, j] for j in range(width) for i in range(height) ]


def new_food(food, snake, dimensions):
    possible_positions = []
    for position in cells(*dimensions):
        if position not in food and position not in snake.full_body:
            possible_positions.append(position)
    return [random.choice(possible_positions)]
    # Или с list comrehension
    #return random.choice([ position for position in cells(*dimensions)
    #    if position not in food and position not in snake ])



def obstacle_ahead(snake, direction, dimensions):
    next_position = move(snake, direction)[-1]
    return is_wall(next_position, dimensions) or is_snake(snake, next_position)


def is_wall(position, dimensions):
    return position[0] >= dimensions[0] or position[1] >= dimensions[1]


def is_food(position, food):
    return position in food


def clear_screen():
    subprocess.call('clear',shell=True)


def read_key(valid_keys = [keys.UP, keys.LEFT, keys.RIGHT, keys.DOWN]):
    key = getkey()
    while key not in valid_keys:
        key = getkey()
    return key


def end_game():
    clear_screen()
    print("Game over!")
    sys.exit(0)


def print_board(snake, food, dimentions):
    width, height = dimentions
    for y in range(height):
        for x in range(width):
            if [x, y] == snake.head:
                print("@", end = " ")
            elif [x, y] in snake.body:
                print("*", end = " ")
            elif [x, y] in food:
                print("#", end = " ")
            else:
                print(" ", end = " ")
        print()


def get_snake_next_direction(current_direction, key):
    if key == keys.UP and current_direction != Direction.DOWN:
        return  Direction.UP
    elif key == keys.DOWN and current_direction != Direction.UP:
        return  Direction.DOWN
    elif key == keys.LEFT and current_direction != Direction.RIGHT:
        return  Direction.LEFT
    elif key == keys.RIGHT and current_direction != Direction.LEFT:
        return  Direction.RIGHT
    return current_direction


class Snake(object):

    def __init__(self, body, direction):
        self.__body = body
        self.direction = direction

    @property
    def head(self):
        return self.__body[-1]

    @property
    def body(self):
        return self.__body[:-1]

    @property
    def full_body(self):
        return self.__body

    def grow(self, direction):
        return Snake(self.__grow(direction), direction)

    def move(self, direction):
        return Snake(self.__move(direction), direction)

    def __grow(self, direction):
        new_head = [self.head[0] + direction[0], self.head[1] + direction[1]]
        if new_head in self.__body:
            raise RuntimeError("Snake cannot grow into itself")
        return self.__body + [new_head]

    def __move(self, direction):
        return self.__grow(direction)[1:]


if __name__ == "__main__":
    dimentions = (10, 10)
    snake = Snake([[5, 5], [5, 4], [5, 3]], Direction.UP)
    food = [[2, 3]]

    while True:
        clear_screen()
        print_board(snake, food, dimentions)
        key = read_key()
        direction = get_snake_next_direction(snake.direction, key)
        try:
            snake = snake.move(direction)
        except RuntimeError as err:
            end_game()
        if is_food(snake.head, food):
            snake = snake.grow(direction)
            food = new_food(food, snake, dimentions)
        elif is_wall(snake.head, dimentions):
            end_game()
