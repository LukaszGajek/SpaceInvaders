import pygame
import keyboard
import time
from player import Player
from player import PlayerBullet
from enemies import Enemy


pygame.init()
width, height = 1000, 500
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Simple Window')
background_color = (200, 200, 200)  

bullets = []
enemies = []

player = Player([width/2,height*0.88]) #x,y

enemies.append(Enemy([width/2,height*0.1]))
enemies.append(Enemy([width/3,height*0.1]))
enemies.append(Enemy([width/4,height*0.1]))
enemies.append(Enemy([width/2.5,height*0.1]))





start = time.monotonic()

running = True
while running:
    
    last = start
    start = time.monotonic()
    delta = start - last
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    if keyboard.is_pressed('a') and player.rect.left >= 0: #obsluga kbm pygamea
        player.shift_left(delta) 
    if keyboard.is_pressed('d') and player.rect.left <= width - player.rect.width:
        player.shift_right(delta)
        
    if keyboard.is_pressed('space'):
        pocisk = player.shoot()
        if pocisk is not None:
            bullets.append(pocisk)

    
     
           
    for bullet in bullets:
        bullet.move(delta)
        if bullet.rect.top <= 0:
            bullet.is_alive = False
      
    for bullet in bullets:
        for enemy in enemies:
            if enemy.rect.colliderect(bullet.rect):
                enemy.get_hit()
                bullet.is_alive = False


      
        
    for enemy in enemies:
        if enemy.hp <= 0:
            enemy.is_alive = False
           
    bullets = [bullet for bullet in bullets if bullet.is_alive]
    enemies = [enemy for enemy in enemies if enemy.is_alive]

    

    screen.fill(background_color)
    screen.blit(player.image,player.rect)
    for bullet in bullets:
        screen.blit(bullet.image,bullet.rect)
    for enemy in enemies:
        screen.blit(enemy.image,enemy.rect)

    

    
    pygame.display.update()
pygame.quit()
