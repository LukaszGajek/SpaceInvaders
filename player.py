import pygame
class Player (pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,50))
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        
        
    def shift_left(self):
        self.rect.left -= 1
    def shift_right(self):
        self.rect.left += 1