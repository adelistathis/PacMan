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
        self.SPEED = 5
        self.WIDTH = 606
        self.HEIGHT = 606
        self.x_speed = 0
        self.y_speed = 0

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

    def move(self, wall_list):

        collision_list = pygame.sprite.spritecollide(self, wall_list, False)

        direction = self.choose_direction()
        if direction == "LEFT":
            self.x_speed = -self.SPEED
            self.y_speed = 0
        if direction == "RIGHT":
            self.x_speed = self.SPEED
            self.y_speed = 0
        if direction == "UP":
            self.y_speed = -self.SPEED
            self.x_speed = 0
        if direction == "DOWN":
            self.y_speed = self.SPEED
            self.x_speed = 0
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH
            self.x_speed = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.x_speed = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.y_speed = 0
        if self.rect.bottom > self.HEIGHT:
            self.rect.bottom = self.HEIGHT
            self.y_speed = 0
        hits = pygame.sprite.spritecollide(self, wall_list, False)
        if hits:
            self.rect.x += -self.x_speed
            self.rect.y += -self.y_speed
            self.x_speed = 0
            self.y_speed = 0
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed





























