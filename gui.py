import pygame, sys

class Main():
    BG = (20,30,40)
    WIDTH = 1000
    HEIGHT = 700

    def __init__(self):
        pygame.init()
        self.active = True
        self.screen = pygame.display.set_mode((Main.WIDTH, Main.HEIGHT))
        self.board = pygame.image.load('assets/cn4brd.png').convert_alpha()
        self.clock = pygame.time.Clock()
        self.game()

    def draw_brd(self):
        self.screen.blit(self.board, (200, 100))

    def game(self):
        
        while self.active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_brd()
            pygame.display.update()
            self.clock.tick(120)
