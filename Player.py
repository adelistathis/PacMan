import pygame

# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    def __init__(self, xIn, yIn ,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.center = (xIn,yIn)


    def update(self):
        self.rect.x += 5
