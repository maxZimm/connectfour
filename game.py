from board import Board
from player import Player
from gameio import GameIO

class Game:

    def __init__(self):
        self.board = Board()
        self.io = GameIO()
        self.players = []

    def get_players(self):
        for i in range(2):
            self.players.append(Player(self.io.get_name()))  

    def player_turn():
        pass

    def main():
        self.get_players()
        # one round of player turns?
        # then a while loop to keep the game going? Or just start the game and check for winner even though no turn has happend
