import pygame
from constants import GRAVITY, FLOOR_Y, DINO_X, VELOCITY

class Dino(pygame.sprite.Sprite):
    def __init__(self, starting_y, img_path):
        pygame.sprite.Sprite.__init__(self)

        self.y = starting_y
        self.velocity = 0
        self.grounded = True

        img = pygame.image.load(img_path).convert_alpha()
        self.image = pygame.transform.scale_by(img, 1.5)
        self.rect = self.image.get_rect()
        self.rect.midbottom = [DINO_X, self.y]
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if self.grounded:
            if keys[pygame.K_SPACE]:
                self.grounded = False
                self.velocity = -VELOCITY

        self.y += self.velocity * dt
        self.velocity += GRAVITY * dt

        # Ground detection
        if self.y >= FLOOR_Y:
            self.velocity = 0
            self.grounded = True
            self.y = FLOOR_Y

        self.rect.midbottom = [DINO_X, self.y]


    def position(self):
        return (DINO_X, self.y)
    
    
    def __str__(self):
        return f"Y: {self.y}\nGrounded: {self.grounded}\n"
