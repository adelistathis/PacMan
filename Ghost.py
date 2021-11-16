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

    def move(self, walls, count):

        collision = pygame.sprite.spritecollide(self, walls, False)

        # first move
        if count <= 1:
            while collision is False:
                self.rect.top -= 1
        else:
            direction = self.choose_direction()
            while collision is False:
                if direction == "UP":
                    self.rect.top -= 1
                elif direction == "DOWN":
                    self.rect.top += 1
                elif direction == "LEFT":
                    self.rect.left -= 1
                elif direction == "RIGHT":
                    self.rect.left += 1

            if direction == "UP":
                self.rect.top += 1
            elif direction == "DOWN":
                self.rect.top -= 1
            elif direction == "LEFT":
                self.rect.left += 1
            elif direction == "RIGHT":
                self.rect.left -= 1





























