from collections import namedtuple


class Turtle(object):

    # UP, RIGHT, DOWN, LEFT
    ORIENTATIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, rows, cols):
        self.canvas = [[0 for col in range(cols)] for row in range(rows)]

        self.__rows = rows
        self.__cols = cols
        self.__orientation = 1
        self.__position = None

    def spawn_at(self, row, col):
        self.__position = [row % self.__rows, col % self.__cols]
        self.canvas[self.__position[0]][self.__position[1]] += 1

    def move(self):
        if self.__position is None:
            raise RuntimeError("Cannot Move!")

        coordinates = Turtle.ORIENTATIONS[self.__orientation]
        row = self.__position[0] + coordinates[0]
        col = self.__position[1] + coordinates[1]
        self.spawn_at(row, col)

    def turn_right(self):
        self.__orientation += 1
        self.__orientation %= len(Turtle.ORIENTATIONS)

    def turn_left(self):
        for _ in range(3):
            self.turn_right()


class SimpleCanvas(object):

    def __init__(self, canvas, symbols):
        self.__canvas = canvas
        self.__symbol_ranges = self.__build_symbol_range_map(symbols)
        self.__max_visits = max([max(row) for row in canvas])

    def draw(self):
        return "\n".join([self.__map_pixels(row) for row in self.__canvas])

    def __map_pixels(self, row):
        return "".join([self.__find_symbol(pixel) for pixel in row])

    def __find_symbol(self, pixel):
        intensity = self.__calculate_intensity(pixel)
        if intensity == 0:
            return self.__symbol_ranges[(0, 0)]
        for symbol_range, symbol in self.__symbol_ranges.items():
            if intensity > symbol_range[0] and intensity <= symbol_range[1]:
                return symbol

    def __calculate_intensity(self, pixel):
        return pixel / self.__max_visits

    def __build_symbol_range_map(self, symbols):
        result = {(0, 0): symbols[0]}
        step = 1 / len(symbols[1:])
        range_begin = 0
        range_end = step
        for symbol in symbols[1:]:
            result[(range_begin, range_end)] = symbol
            range_begin = range_end
            range_end += step
        return result
