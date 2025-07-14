import pygame
import time
import random
import math
from space_invaders.player import Life


class Enemy(pygame.sprite.Sprite):

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/enemy1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.last_shot_time = 0
        self.last_try_time = 0
        self.original_position_horizontal = self.rect.left
        self.original_position_vertical = self.rect.top
        self.start_left = random.randint(0,1) # 1 to prawo
        self.time = 0
        self.is_diving = False
        self.is_ascending = False
        self.last_state_change_time = 0
        self.state = 0

        self.hp = 3
        self.is_alive = True

    def get_hit(self):
        self.hp -= 1
        if self.hp == 2:
            self.image = pygame.image.load("assets/enemy1_yellow.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 50))

        elif self.hp == 1:
            self.image = pygame.image.load("assets/enemy1_red2.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 50))

    def shoot(self):
        rand = random.randint(-150, 150)
        shooting_randomizer = random.randint(0, 1000)
        last = self.last_shot_time
        delta = time.monotonic() - last
        if delta > 1 and shooting_randomizer >= 995:
            self.last_shot_time = time.monotonic()
            return EnemyBullet(
                [self.rect.left + 25, self.rect.top + 20], rand
            )  # zmienić
        else:
            return None

    def drop_life(self):
        return Life([self.rect.left + 25, self.rect.top])

    def move(self, delta):
        self.time += delta

        if self.start_left == 1:
            self.rect.left = (
                math.sin(3 * self.time / 2 * math.pi) * -100 + self.original_position_horizontal
            )
        else:
            self.rect.left = (
                math.sin(3 * self.time / 2 * math.pi) * 100 + self.original_position_horizontal
            )
        # if self.rect.left <= self.original_position + 100  and self.dir == 1 and self.rect.left <= 1000:
        #     self.rect.left += 100*delta
        # elif self.rect.left > self.original_position + 100  and self.dir == 1:
        #     self.dir = 0
        # elif self.rect.left >= self.original_position - 100  and self.dir == 0 and self.rect.left >= 0:
        #      self.rect.left -= 100*delta
        # elif self.rect.left < self.original_position - 100  and self.dir == 0:
        #     self.dir = 1

    def start_tweaking(self):
        tweak_bullets = []
       

        
        # self.last_state_change_time = time.monotonic()
        # last = self.last_state_change_time

        # while delta < 3:
        #     delta = time.monotonic() - last
        while len(tweak_bullets) < 5:
            proj = self.shoot()
            if proj != None:
                tweak_bullets.append(proj)
            self.last_shot_time = 0
            
        return tweak_bullets
    
    def dive(self,delta):
        
        if self.rect.top < 500 and self.is_diving == True:
            self.rect.top += 200*delta
        if self.rect.top >= 500 and self.is_ascending == False:
            self.is_diving = False
            self.is_ascending = True
            
    def ascend(self,delta):
        
        if self.rect.top > self.original_position_vertical and self.is_ascending == True:
            self.rect.top -= 200*delta
        if self.rect.top <= self.original_position_vertical and self.is_diving == False:
            self.is_ascending = False
        
        
        
            
        
            
            
            

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, position, shot_angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/enemy_bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 35))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.is_alive = True
        self.shot_angle = shot_angle

    def move(self, delta):
        self.rect.top += 300 * delta
        self.rect.left += self.shot_angle * delta
