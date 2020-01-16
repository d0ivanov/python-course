import unittest
import solution

from solution import TicTacToeBoard

class SolutionTest(unittest.TestCase):

    def test_move_when_cell_number_before_letter_raises(self):
        board = TicTacToeBoard()
        with self.assertRaises(solution.InvalidKey):
            board["1B"] = "X"

    def test_move_when_cell_is_just_a_letter(self):
        board = TicTacToeBoard()
        with self.assertRaises(solution.InvalidKey):
            board["B"] = "X"

    def test_move_when_cell_is_just_a_number(self):
        board = TicTacToeBoard()
        with self.assertRaises(solution.InvalidKey):
            board["1"] = "X"

    def test_move_when_cell_is_invalid_letter(self):
        board = TicTacToeBoard()
        with self.assertRaises(solution.InvalidKey):
            board["Z"] = "X"

    def test_move_when_cell_is_invalid_number(self):
        board = TicTacToeBoard()
        with self.assertRaises(solution.InvalidKey):
            board["9"] = "X"

    def test_move_when_cell_has_invalid_letter(self):
        board = TicTacToeBoard()
        with self.assertRaises(solution.InvalidKey):
            board["D1"] = "X"

    def test_move_when_cell_has_invalid_number(self):
        board = TicTacToeBoard()
        with self.assertRaises(solution.InvalidKey):
            board["B8"] = "X"

    def test_move_when_invalid_value(self):
        board = TicTacToeBoard()
        with self.assertRaises(solution.InvalidValue):
            board["B3"] = "d"

    def test_can_move_when_cell_valid(self):
        board = TicTacToeBoard()
        board["B1"] = "X"
        board["C1"] = "O"
        self.assertEqual(board["B1"], "X")
        self.assertEqual(board["C1"], "O")

    def test_move_twice_on_same_cell(self):
        board = TicTacToeBoard()
        with self.assertRaises(solution.InvalidMove):
            board["A1"] = 'X'
            board["A1"] = 'O'

    def test_move_twice_with_same_value(self):
        board = TicTacToeBoard()
        with self.assertRaises(solution.NotYourTurn):
            board["A1"] = 'X'
            board["B1"] = 'X'

    def test_game_in_progress_when_board_instantiated(self):
        board = TicTacToeBoard()
        self.assertEqual("Game in progress.", board.game_status())

    def test_print_empty_board(self):
        board = TicTacToeBoard()
        empty_board = """
  -------------
3 |   |   |   |
  -------------
2 |   |   |   |
  -------------
1 |   |   |   |
  -------------
    A   B   C
"""
        self.assertEqual(empty_board.strip(), str(board).strip())

    def test_print_full_board(self):
        board = TicTacToeBoard()
        board_str = """
  -------------
3 | X | X | X |
  -------------
2 | O | O | X |
  -------------
1 | O | X | O |
  -------------
    A   B   C
"""
        board["A3"] = "X"
        board["A2"] = "O"
        board["B3"] = "X"
        board["B2"] = "O"
        board["C3"] = "X"
        board["C1"] = "O"
        board["C2"] = "X"
        board["A1"] = "O"
        board["B1"] = "X"
        self.assertEqual(board_str.strip(), str(board).strip())

    def test_x_wins(self):
        board = TicTacToeBoard()
        board["A3"] = "X"
        board["C3"] = "O"
        board["B2"] = "X"
        board["B1"] = "O"
        board["C1"] = "X"

        self.assertEqual("X wins!", board.game_status())

    def test_o_wins(self):
        board = TicTacToeBoard()
        board["C3"] = "O"
        board["A3"] = "X"
        board["B2"] = "O"
        board["B1"] = "X"
        board["A1"] = "O"

        self.assertEqual("O wins!", board.game_status())

    def test_draw(self):
        board = TicTacToeBoard()
        board["A1"] = 'O'
        board["B1"] = 'X'
        board["A3"] = 'O'
        board["A2"] = 'X'
        board["C2"] = 'O'
        board["C3"] = 'X'
        board["B3"] = 'O'
        board["B2"] = 'X'
        board["C1"] = 'O'

        self.assertEqual('Draw!', board.game_status())

    def test_game_in_progress(self):
        board = TicTacToeBoard()
        board["A1"] = 'X'
        board["A3"] = 'O'

        self.assertEqual('Game in progress.', board.game_status())

if __name__ == "__main__":
    unittest.main()
