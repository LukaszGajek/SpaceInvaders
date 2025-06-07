import pygame
import time
class Player (pygame.sprite.Sprite):
    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,50))
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.last_shot_time = 0
        self.hp = 3
        
        
    def shift_left(self, delta):
        self.rect.left -= 800 * delta
    def shift_right(self, delta):
        self.rect.left += 800 * delta
        
    def shoot(self):
        last = self.last_shot_time
        delta = time.monotonic() - last
        if delta > 0.35:
            self.last_shot_time = time.monotonic()
            return PlayerBullet([self.rect.left + 25, self.rect.top - 70]) #zmienić
        else:
            return None
    def get_hit(self):
        self.hp -= 1
    def get_healed(self):
        self.hp += 1

    
        

            
class PlayerBullet (pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player_bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,80))
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.is_alive = True

    
    def move(self, delta):
        self.rect.top -=500*delta

class Life (pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/heart.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.is_alive = True
    
    def move(self,delta):
        self.rect.top += 250*delta