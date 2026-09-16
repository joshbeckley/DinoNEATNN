import pygame

class Ground(pygame.sprite.Sprite):

    def __init__(self, x, y, img_path):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(img_path).convert_alpha()
        self.image = pygame.transform.scale_by(img, 1.5)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]