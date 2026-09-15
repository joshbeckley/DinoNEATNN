import pygame
from constants import GRAVITY, FLOOR_Y, DINO_X, VELOCITY

class Dino:
    def __init__(self, starting_y, img_path):
        self.y = starting_y
        self.velocity = 0
        self.grounded = True
        img = pygame.image.load(img_path).convert_alpha()
        self.img = pygame.transform.scale(img, (200, 200))
    
    def update(self):
        keys = pygame.key.get_pressed()
        
        if self.grounded:
            if keys[pygame.K_SPACE]:
                self.grounded = False
                self.velocity = -VELOCITY

        self.y += self.velocity
        self.velocity += GRAVITY

        # Ground detection
        if self.y >= FLOOR_Y:
            self.velocity = 0
            self.grounded = True
            self.y = FLOOR_Y


    def position(self):
        return (DINO_X, self.y)
    
    
    def __str__(self):
        return f"Y: {self.y}\nGrounded: {self.grounded}\n"
