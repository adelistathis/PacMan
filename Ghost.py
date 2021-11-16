import random
import os
import pygame.sprite

from Wall import Wall

class Ghost(pygame.sprite.Sprite):

    def __init__(self, fileName, x, y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('images', fileName))
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def move(self, walls):
        speed = 2 # 2 pixels per move

        dx = random.choice([-speed, speed])
        dy = random.choice([-speed, speed])

        self.rect.left += dx
        self.rect.top += dy

        collision = pygame.sprite.spritecollide(self, walls, False)

        while collision:
            self.rect.left -= dx
            self.rect.top -= dy

            dx = random.choice([-speed, speed])
            dy = random.choice([-speed, speed])

            self.rect.left += dx
            self.rect.top += dy

            collision = pygame.sprite.spritecollide(self, walls, False)












