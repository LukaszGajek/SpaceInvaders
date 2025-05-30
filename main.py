import pygame


pygame.init()
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Window')
background_color = (200, 200, 200)  # Light gray

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)
    pygame.display.flip()

pygame.quit()
