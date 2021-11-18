import random
import os
import pygame.sprite


class Ghost(pygame.sprite.Sprite):

    def __init__(self, fileName, x, y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load(os.path.join('images', fileName))
        self.image = pygame.transform.scale(image, (30, 30))

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.direction = "UP"

    def choose_direction(self):
        a = random.randint(1, 4)

        if a == 1:
            return "UP"
        elif a == 2:
            return "DOWN"
        elif a == 3:
            return "LEFT"
        elif a == 4:
            return "RIGHT"

    def move(self, walls):

        collision = pygame.sprite.spritecollide(self, walls, False)

        if self.direction == "UP":
            self.rect.top -= 1
            while collision:
                self.rect.top += 1

            self.direction = self.choose_direction()
        elif self.direction == "DOWN":
            self.rect.top += 1
            while collision:
                self.rect.top -= 1

            self.direction = self.choose_direction()
        elif self.direction == "LEFT":
            self.rect.left -= 1
            while collision:
                self.rect.left += 1

            self.direction = self.choose_direction()
        elif self.direction == "RIGHT":
            self.rect.left += 1
            while collision:
                self.rect.left -= 1

            self.direction = self.choose_direction()





























