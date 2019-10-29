import random
import time
from getkey import getkey, keys
import subprocess

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

UP = [0, -1]
DOWN = [0, 1]
RIGHT = [1, 0]
LEFT = [-1, 0]


def cells(width, height):
    cells = []
    for i in range(width):
        for j in range(height):
            cells.append([i, j])
    return cells
    # Или с list comprehension
    #return [ [i, j] for j in range(width) for i in range(height) ]


def grow(snake, direction):
    return snake + [[snake[-1][0] + direction[0], snake[-1][1] + direction[1]]]


def move(snake, direction):
    return grow(snake, direction)[1:]


def new_food(food, snake, dimensions):
    possible_positions = []
    for position in cells(*dimensions):
        if position not in food and position not in snake:
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


def is_snake(position, snake):
    return position in snake


def clear_screen():
    subprocess.call('clear',shell=True)


def read_key(valid_keys = [keys.UP, keys.LEFT, keys.RIGHT, keys.DOWN]):
    key = getkey()
    while key not in valid_keys:
        key = getkey()
    return key


def print_board(snake, food, width, height):
    for y in range(height):
        for x in range(width):
            if [x, y] in snake:
                if [x, y] == snake[-1]:
                    print("[ @  ]", end = " ")
                else:
                    print("[ *  ]", end = " ")
            elif [x, y] in food:
                print("[ #  ]", end = " ")
            else:
                print("[{}, {}]".format(x, y), end = " ")
        print()


if __name__ == "__main__":
    width, height = 10, 10
    snake = [[5, 5], [5, 4], [5, 3]]
    food = [[2, 3]]
    last_direction = UP

    while True:
        clear_screen()
        print_board(snake, food, width, height)
        k = read_key()
        if k == keys.UP and last_direction != DOWN:
            snake = move(snake, UP)
            last_direction = UP
        elif k == keys.DOWN and last_direction != UP:
            snake = move(snake, DOWN)
            last_direction = DOWN
        elif k == keys.LEFT and last_direction != RIGHT:
            snake = move(snake, LEFT)
            last_direction = LEFT
        elif k == keys.RIGHT and last_direction != LEFT:
            snake = move(snake, RIGHT)
            last_direction = RIGHT
        if snake[-1] in food:
            snake = grow(snake, last_direction)
            food = new_food(food, snake, (width, height))


