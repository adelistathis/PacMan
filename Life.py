import pygame
import os


class Life(pygame.sprite.Sprite):
    def __init__(self, fileName, xIn, yIn):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(os.path.join('images', fileName))
        self.image = pygame.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (xIn, yIn)
