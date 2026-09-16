# Example file showing a circle moving on screen
import pygame
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, FLOOR_Y, FPS
from dino import Dino
from environment import Environment

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock()

dino = Dino(FLOOR_Y, "dino.png")
environment = Environment(screen, dino)

dt = 0
clock.tick(FPS)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False


    dino.update(dt)
    environment.draw()
    
    
    print(dino)


    dt = clock.tick(FPS) / 1000.0

pygame.quit()