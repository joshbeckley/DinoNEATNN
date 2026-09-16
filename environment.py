import pygame
from constants import FLOOR_Y, DINO_X
class Environment:

    def __init__(self, screen, dino):
        self.screen = screen
        self.dino = dino
        raw_plane = pygame.image.load("plane.png").convert_alpha()
        self.plane_img = pygame.transform.scale(raw_plane, (2000, raw_plane.get_height()))
    
    def draw(self):
        self.screen.fill("white")

        self.screen.blit(self.plane_img, (0, FLOOR_Y))
        self.screen.blit(self.dino.img, (DINO_X - self.dino.img_size[0], self.dino.y - self.dino.img_size[1]*2))

        pygame.display.flip()