import pygame
import keyboard

from player import Player

pygame.init()
width, height = 1000, 500
screen = pygame.display.set_mode((width, height))
#player = pygame.image.load('C:/Szkoła/Informatyka/Python/SpaceInvaders/assets/player.png')

pygame.display.set_caption('Simple Window')
background_color = (200, 200, 200)  # Light gray

gracz = Player([300,440]) #x,y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    try:
        if keyboard.is_pressed('a'):
            gracz.shift_left() 
            pygame.time.delay(2)
        if keyboard.is_pressed('d'):
            gracz.shift_right()
            pygame.time.delay(2)

    except:
        pass
     
    #gracz.shift_left() 

           
    screen.fill(background_color)
    screen.blit(gracz.image,gracz.rect)
    
    pygame.display.update()

pygame.quit()
