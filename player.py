import pygame
class Player (pygame.sprite.Sprite):
    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,50))
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        
        
    def shift_left(self):
        self.rect.left -= 2
    def shift_right(self):
        self.rect.left += 2
        
    def shoot(self):
        return PlayerBullet([self.rect.left + 25, self.rect.top - 70])
        

            
class PlayerBullet (pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player_bullet1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,80))
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
    
    def move(self):
        self.rect.top -=1