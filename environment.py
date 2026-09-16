import pygame
from constants import FLOOR_Y, DINO_X
from cactus import Cactus
from ground import Ground

class Environment:

    def __init__(self, screen, dino):
        self.screen = screen
        self.dino = dino

        self.dino_group = pygame.sprite.Group()
        self.dino_group.add(self.dino)

        cactus = Cactus(500, FLOOR_Y, "assets/cactus.png")
        self.cactus_group = pygame.sprite.Group()
        self.cactus_group.add(cactus)

        self.ground = Ground(0, FLOOR_Y, "assets/ground.png")
        # TODO: could move in draw
        self.ground_group = pygame.sprite.Group()
        self.ground_group.add(self.ground)
        
    
    def draw(self):
        self.screen.fill("white")

        self.dino_group.draw(self.screen)
        self.cactus_group.draw(self.screen)
        self.ground_group.draw(self.screen)

        pygame.display.update()

    def update(self, dt):
        self.dino_group.update(dt)
        self.cactus_group.update()
        