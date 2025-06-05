import pygame
import keyboard

from player import Player
from player import PlayerBullet



pygame.init()
width, height = 1000, 500
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Simple Window')
background_color = (200, 200, 200)  

bullets = []

gracz = Player([width/2,height*0.88]) #x,y



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    try:
        if keyboard.is_pressed('a') and gracz.rect.left >= 0:
            gracz.shift_left() 
        if keyboard.is_pressed('d') and gracz.rect.left <= width - 100:
            gracz.shift_right()
            
        if keyboard.is_pressed('space') and len(bullets) < 1:
            pocisk = gracz.shoot()
            bullets.append(pocisk)
            pygame.time.delay(2)

    except:
        pass
     
           
    for bullet in bullets:
        bullet.move()
        if bullet.rect.top <= 0:
            bullets.remove(bullet)   
        
       
           
    
    screen.fill(background_color)
    screen.blit(gracz.image,gracz.rect)
    for bullet in bullets:
        screen.blit(bullet.image,bullet.rect)

    

    
    pygame.display.update()
    pygame.time.delay(2)

pygame.quit()
