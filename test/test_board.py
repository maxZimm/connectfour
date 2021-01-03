import unittest
import sys
sys.path.append('..')
from board import Board

class TestBoardMethods(unittest.TestCase):

    def test_accept_move(self):
        board = Board()
        board.accept_move(('player1', 4))
        self.assertEqual(board.state[5][4],  'player1')
        board.accept_move(('player2', 4))
        self.assertEqual(board.state[4][4],  'player2')
        board.accept_move(('player1', 4))
        board.accept_move(('player1', 4))
        board.accept_move(('player1', 4))
        board.accept_move(('player1', 4))
        board.accept_move(('player2', 4))
        self.assertEqual(board.state[0][4],  'player1')
        board.accept_move(('player2', 6))
        self.assertEqual(board.state[5][6],  'player2')
        board.accept_move(('player1', 6))
        self.assertEqual(board.state[5][6],  'player2')

    def test_check_row_win(self):
        board = Board()
        board.accept_move(('player1', 2))
        board.accept_move(('player1', 3))
        board.accept_move(('player1', 4))
        board.accept_move(('player1', 5))
        self.assertEqual(board.check_row_win(board.state[5]), 'player1')
        board.accept_move(('player2', 0))
        board.accept_move(('player2', 1))
        board.state[5][2] = 'player2'
        self.assertEqual(board.check_row_win(board.state[5]),None)

    def test_check_col_win(self):
        board = Board()
        board.accept_move(('player1', 2))
        board.accept_move(('player1', 2))
        board.accept_move(('player1', 2))
        board.accept_move(('player1', 2))
        self.assertEqual(board.check_col_win(2), 'player1')
        board.accept_move(('player2', 3))
        board.accept_move(('player2', 3))
        board.accept_move(('player1', 3))
        board.accept_move(('player1', 3))
        board.accept_move(('player1', 3))
        board.accept_move(('player1', 3))
        self.assertEqual(board.check_col_win(3), 'player1')
        self.assertEqual(board.check_col_win(4), None)

    def test_diag_win(self):
        board = Board()
        board.state[4][1] = 'player1'
        board.state[3][2] = 'player1'
        board.state[2][3] = 'player1'
        board.state[1][4] = 'player1'
        self.assertEqual(board.check_diag_win(), 'player1')
        board.state[4][3] = 'player2'
        board.state[3][2] = 'player2'
        board.state[2][1] = 'player2'
        board.state[1][0] = 'player2'
        self.assertEqual(board.check_diag_win(), 'player2')

    def test_check_winner(self):
        board = Board()
        self.assertEqual(board.check_winner(), None)
        board.state[4][3] = 'player2'
        board.state[3][2] = 'player2'
        board.state[2][1] = 'player2'
        board.state[1][0] = 'player2'
        self.assertEqual(board.check_winner(), 'player2')
        board.state[3][2] = 'player1'
        board.state[3][3] = 'player1'
        board.state[3][4] = 'player1'
        board.state[3][5] = 'player1'
        self.assertEqual(board.check_winner(), 'player1')

if __name__ == '__main__':
    unittest.main()

