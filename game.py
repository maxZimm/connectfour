from board import Board
from player import Player
from gameio import GameIO
import pygame, sys

class Game:
    WIDTH = 1000
    HEIGHT = 700
    BG = (40,50,60)

    def __init__(self):
        self.board = Board()
        self.io = GameIO()
        self.players = []
        pygame.init()
        self.screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.clock = pygame.time.Clock()
        self.board_img = pygame.image.load('assets/cn4brd.png').convert_alpha()
        self.chips = []

    def get_players(self):
        for i in range(1,3):
            self.players.append(Player(self.io.get_name(i)))  

    def player_turn(self, player):
        self.board.accept_move((player, self.io.get_move(player)))

    def main(self):
        #self.get_players()
        turn = 0
        self.chips.append(Chip(1,self.screen))
        self.chips.append(Chip(2,self.screen))
        while not self.board.check_winner():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(Game.BG)
            for c in self.chips:
                c.draw()
            self.screen.blit(self.board_img, (200,95))
            pygame.display.update()
            self.clock.tick(120)
           # self.io.cli_clrscrn()
           # self.io.print_board(self.board)
           # self.player_turn(self.players[turn % 2])
           # turn += 1
       # self.io.cli_clrscrn()
       # self.io.print_board(self.board)
       # print(f"Player {self.board.check_winner().name} wins!")

class Chip():

    def __init__(self, player, screen):
        if player == 1:
            self.chip = pygame.image.load('assets/bluechip.png').convert_alpha()
            self.rect = self.chip.get_rect(center = (100,400))
        elif player == 2:
            self.chip = pygame.image.load('assets/redchip.png').convert_alpha()
            self.rect = self.chip.get_rect(center = (900,400))

        self.player = player
        self.screen = screen
        self.active = 1

    def draw(self):
        self.screen.blit(self.chip, self.rect)
if __name__ == '__main__':
    Game().main()
