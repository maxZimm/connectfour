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
        self.slots = []

    def get_players(self):
        for i in range(1,3):
            self.players.append(Player(self.io.get_name(i)))  

    def player_turn(self, player):
        self.board.accept_move((player, self.io.get_move(player)))

    def build_slots(self):
        for i in range(7):
            self.slots.append(Slot(i, self.screen))

    def build_chips(self):
        if not self.chips:
            self.chips.append(Chip(1, self.screen))
            self.chips.append(Chip(2, self.screen))
        else:
            for c in self.chips:
                if c.active == 0:
                    self.chips.append(Chip(c.player, self.screen))
                    self.chips.remove(c)

    def main(self):
        #self.get_players()
        turn = 0
        self.build_slots()
        while not self.board.check_winner():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.build_chips()
            self.screen.fill(Game.BG)
            for s in self.slots:
                s.draw()
            for c in self.chips:
                c.move(self.slots)
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

    def move(self, ss):
        if self.active == 1:
            mouse = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()
            if self.rect.left < mouse[0] < self.rect.right and self.rect.top < mouse[1] < self.rect.bottom and pressed[0] == 1:
                self.rect = self.chip.get_rect(center = mouse)
                self.draw()
            else:
                if not self.slot_col(ss):
                    self.draw()

    def slot_col(self, ss):
        mouse = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        for s in ss:
            if s.rect.colliderect(self.rect) and pressed[0] == 0:
                print(f'We got a hit on {s.ind}')
                self.active = 0
                return True

class Slot():

    def __init__(self, ind, screen):
        self.ind = ind
        self.color = (60,70,100)
        self.rect = pygame.Rect(205 + (self.ind * 85),0, 75,100)
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color , self.rect)

if __name__ == '__main__':
    Game().main()
