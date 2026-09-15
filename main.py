# Example file showing a circle moving on screen
import pygame
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, FLOOR_Y
from dino import Dino

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

running = True
dino = Dino(FLOOR_Y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    screen.fill("purple")

    pygame.draw.circle(screen, "red", dino.position(), 40)

    dino.update()

    
    print(dino)

    pygame.time.delay(30)
    pygame.display.flip()

pygame.quit()