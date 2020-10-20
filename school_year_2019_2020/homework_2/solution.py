from itertools import product

class InvalidMove(Exception): pass

class InvalidValue(Exception): pass

class InvalidKey(Exception): pass

class NotYourTurn(Exception): pass

class TicTacToeBoard:

    VALID_CELLS = ["ABC", "123"]
    VALID_MOVES = "OX"
    BOARD_REPR = """
  -------------
3 |{A3:^3}|{B3:^3}|{C3:^3}|
  -------------
2 |{A2:^3}|{B2:^3}|{C2:^3}|
  -------------
1 |{A1:^3}|{B1:^3}|{C1:^3}|
  -------------
    A   B   C
"""

    def __init__(self):
        self.__board = {k: "" for k in self.__valid_cells()}
        self.__turn = ""

    def __str__(self):
        return TicTacToeBoard.BOARD_REPR.format(**self.__board)

    def __getitem__(self, key):
        return self.__board[key]

    def __setitem__(self, cell, move):
        self.__validate_move(cell, move)
        self.__turn = move
        self.__board[cell] = move

    def game_status(self):
        if self.__is_winner("X"):
            return "X wins!"
        if self.__is_winner("O"):
            return "O wins!"
        if "" in self.__board.values():
            return "Game in progress."
        return "Draw!"

    def __valid_cells(self):
        return ["{}{}".format(x, y) for (x, y) in
                product(*TicTacToeBoard.VALID_CELLS)]

    def __validate_move(self, cell, move):
        if cell not in self.__valid_cells():
            raise InvalidKey
        if move not in TicTacToeBoard.VALID_MOVES:
            raise InvalidValue
        if self.__board[cell] is not "":
            raise InvalidMove
        if self.__turn != "" and self.__turn == move:
            raise NotYourTurn

    def __is_winner(self, player):
        coords = self.__valid_cells()
        all_cells = [self.__values(coords[i:9:3]) for i in [0, 1, 2]] +\
                [self.__values(coords[i:i+3]) for i in [0, 3, 6]] +\
                [self.__values(coords[0:12:4]), self.__values(coords[2:8:2])]

        for cells in all_cells:
            if all([cell == player for cell in cells]):
                return True
        return False

    def __values(self, cells):
        return [self.__board[cell] for cell in cells]
