import pygame
import keyboard
import time
import random

from player import Player
from player import PlayerBullet
from player import Life
from enemies import Enemy


pygame.init()
width, height = 1000, 500
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Simple Window')
background_color = (200, 200, 200)  

bullets = []
enemies = []
player_health = []
projectiles = []
drops = []

player = Player([width/2,height*0.92]) #x,



enemies.append(Enemy([width/2,height*0.2]))
enemies.append(Enemy([width/3,height*0.15]))
enemies.append(Enemy([width/4,height*0.1]))
enemies.append(Enemy([width/2.5,height*0.25]))



start = time.monotonic()

running = True
while running:
    
    last = start
    start = time.monotonic()
    delta = start - last
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player_health = []
    
    for i in range(player.hp):
        player_health.append(Life([5 + i * 40, 10]))
    
    if keyboard.is_pressed('a') and player.rect.left >= 0: #obsluga kbm pygamea
        player.shift_left(delta) 
    if keyboard.is_pressed('d') and player.rect.left <= width - player.rect.width:
        player.shift_right(delta)
        
    if keyboard.is_pressed('space'):
        pocisk = player.shoot()
        if pocisk is not None:
            bullets.append(pocisk)


    


    for enemy in enemies:
        proj = enemy.shoot()
        if proj is not None:
            projectiles.append(proj)
     
           
    for bullet in bullets:
        bullet.move(delta)
        if bullet.rect.top <= 0:
            bullet.is_alive = False
            
            
    for bullet in bullets:
        for enemy in enemies:
            if enemy.rect.colliderect(bullet.rect):
                enemy.get_hit()
                bullet.is_alive = False
    
    for projectile in projectiles:
        projectile.move(delta) 
        if projectile.rect.top >= height:
            projectile.is_alive = False
    
    for projectile in projectiles:
        if projectile.rect.colliderect(player.rect):
            player.get_hit()
            projectile.is_alive = False
            if player.hp == 0:
                running = False
        
    for enemy in enemies:
        if enemy.hp <= 0:
            enemy.is_alive = False
            rand = random.randint(0,3)
            if rand == 2:
                drop = enemy.drop_life()
                drops.append(drop)
                
    for enemy in enemies:
        enemy.move(delta)
                
    for drop in drops:
        drop.move(delta)
        if drop.rect.top >= height:
            drop.is_alive = False
            
    for drop in drops:
        if drop.rect.colliderect(player.rect):
            player.get_healed()
            drop.is_alive = False
            
           
    bullets = [bullet for bullet in bullets if bullet.is_alive]
    enemies = [enemy for enemy in enemies if enemy.is_alive]
    projectiles = [projectile for projectile in projectiles if projectile.is_alive]
    drops = [drop for drop in drops if drop.is_alive]
    

    screen.fill(background_color)
    
    screen.blit(player.image,player.rect)
    for bullet in bullets:
        screen.blit(bullet.image,bullet.rect)
    for enemy in enemies:
        screen.blit(enemy.image,enemy.rect)
    for hp in player_health:
        screen.blit(hp.image,hp.rect)
    for projectile in projectiles:
            screen.blit(projectile.image,projectile.rect)
    for drop in drops:
            screen.blit(drop.image, drop.rect)




    

    
    pygame.display.update()
pygame.quit()
