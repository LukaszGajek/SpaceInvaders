import pygame
import time

class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/main_menu.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (1000, 500))
        self.position = [0,0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.position
        self.state = 0
        self.starting_time = 0
        #self.time = time.monotonic() - self.starting_time

    def begin_game(self):
        self.state = 1
    def end_game(self):
        self.state = 0
        