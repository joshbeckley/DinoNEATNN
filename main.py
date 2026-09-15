# Example file showing a circle moving on screen
import pygame
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, FLOOR_Y, DINO_X
from dino import Dino

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

running = True
dino = Dino(FLOOR_Y, "dino.png")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    screen.fill("white")

    pygame.draw.circle(screen, "red", dino.position(), 40)
    pygame.draw.line(screen, "black", (0, FLOOR_Y), (WINDOW_WIDTH, FLOOR_Y), 5)
    screen.blit(dino.img, (DINO_X, dino.y))

    dino.update()
    
    print(dino)

    pygame.time.delay(30)
    pygame.display.flip()

pygame.quit()