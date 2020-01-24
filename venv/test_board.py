import unittest
from board import Board
from find_best_move import find_best_move

board = Board()


class MyTestCase(unittest.TestCase):

    def test_start(self):
        legal_moves = [0,1,2,3,4,5,6,7,8]
        self.assertEqual(board.legal_moves(),legal_moves)

        board.board[0] = 'X'
        legal_moves = [1,2,3,4,5,6,7,8]
        self.assertEqual(board.legal_moves(),legal_moves)

    def test_last_move(self):
        board = Board()
        # X O -
        # - O -
        # O X X
        board.board[0] = 'X'
        board.board[1] = 'O'
        board.board[4] = 'O'
        board.board[6] = 'O'
        board.board[7] = 'X'
        board.board[8] = 'X'

        legal_moves = [2,3,5]
        self.assertEqual(board.legal_moves(),legal_moves)

        # X O X
        # - O -
        # O X X
        board.board[2] = 'X'
        board.current_player = 'O'

        best_move = 5
        self.assertEqual(find_best_move(board),best_move)

    def test_depth(self):
        board = Board()
        # X X O           X X O
        # - O -           - O -
        # - - -           - X -
        board.board[0] = 'X'
        board.board[1] = 'X'
        board.board[2] = 'O'
        board.board[4] = 'O'

        legal_moves = [3,5,6,7,8]
        self.assertEqual(board.legal_moves(),legal_moves)

        board.board[7] = 'X'
        board.current_player = 'O'

        best_move = 6 # best way to the shortest win
        self.assertEqual(find_best_move(board),best_move)


if __name__ == '__main__':
    unittest.main()
