import pygame
import time
import random
from player import Life




class Enemy (pygame.sprite.Sprite):
    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/enemy1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,50))
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.last_shot_time = 0
        self.last_try_time = 0
        self.original_position= self.rect.left
        self.dir = random.randint(0,1) #1 to prawo

        self.hp = 3
        self.is_alive = True
        
    def get_hit(self):
            self.hp -= 1
            if self.hp == 2:
                    self.image = pygame.image.load('assets/enemy1_pink.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, (100,50))

            elif self.hp == 1:
                self.image = pygame.image.load('assets/enemy1_red.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (100,50))



            
    def shoot(self):
        rand = random.randint(-150,150)
        shooting_randomizer = random.randint(0,1000)
        last = self.last_shot_time
        delta = time.monotonic() - last
        if delta > 1 and shooting_randomizer >= 995:
            self.last_shot_time = time.monotonic()
            return EnemyBullet([self.rect.left + 25, self.rect.top + 20], rand) #zmienić
        else:
            return None
            
        
    def drop_life(self):
        return Life([self.rect.left + 25, self.rect.top])
    
    def move(self, delta):
        if self.rect.left <= self.original_position + 100  and self.dir == 1 and self.rect.left <= 1000:
            self.rect.left += 100*delta
        elif self.rect.left > self.original_position + 100  and self.dir == 1:
            self.dir = 0
        elif self.rect.left >= self.original_position - 100  and self.dir == 0 and self.rect.left >= 0: 
             self.rect.left -= 100*delta
        elif self.rect.left < self.original_position + 100  and self.dir == 0:
            self.dir = 1

    
    
    
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, position, shot_angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/enemy_bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,35))
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.is_alive = True
        self.shot_angle = shot_angle
    
    def move(self, delta):
        self.rect.top += 300*delta
        self.rect.left += self.shot_angle*delta
    
    