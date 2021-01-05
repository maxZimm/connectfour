from board import Board
from player import Player
from gameio import GameIO
import argparse

parser = argparse.ArgumentParser(description='Gui Or CLI')
parser.add_argument('-gui', '-g', nargs=1, default='y')
args = parser.parse_args()
gui = args.gui[0] if args.gui[0] == 'y' else 'n'

class Game:

    def __init__(self, gui):
        self.board = Board()
        self.io = GameIO(gui)
        self.gui = gui
        self.players = []

    def get_players(self):
        if self.gui == 'y':
            for i in range(1,3):
                self.players.append(Player(f'Player {i}'))  
        else:
            for i in range(1,3):
                self.players.append(Player(self.io.get_name(i)))  

    def player_turn(self, player):
        self.board.accept_move((player, self.io.get_move(player)))

    def main(self):
        self.get_players()
        turn = 0
        while not self.board.check_winner():
            self.io.cli_clrscrn()
            self.io.print_board(self.board)
            self.player_turn(self.players[turn % 2])
            turn += 1
        self.io.cli_clrscrn()
        self.io.print_board(self.board)
        print(f"Player {self.board.check_winner().name} wins!")

if __name__ == '__main__':
    Game(gui).main()
