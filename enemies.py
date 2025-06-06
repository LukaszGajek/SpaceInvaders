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
            
    def shoot(self):
        last = self.last_shot_time
        delta = time.monotonic() - last
        if delta > 2:
            self.last_shot_time = time.monotonic()
            return EnemyBullet([self.rect.left + 25, self.rect.top + 70]) #zmienić
        else:
            return None
    
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/enemy_bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.is_alive = True
    
    def move(self, delta):
        self.rect.top +=150*delta