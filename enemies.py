import pygame
import time
class Enemy (pygame.sprite.Sprite):
    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/enemy1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,50))
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.last_shot_time = 0
        self.hp = 3
        self.is_alive = True
        
    def get_hit(self):
            self.hp -= 1