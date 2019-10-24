import random
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

UP = [0, 1]
DOWN = [0, -1]
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
    curr_head = snake[-1]
    new_head = [curr_head[0] + direction[0], curr_head[1] + direction[1]]
    return snake + new_head


def move(snake, direction):
    return grow(snake, direction)[1:]


def new_food(food, snake, dimensions):
    possible_positions = []
    for position in cells(*dimensions):
        if position not in food and position not in snake:
            possible_positions.append(position)
    return random.choice(possible_positions)
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

