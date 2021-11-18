import pygame
import os

# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    def __init__(self, fileName, xIn, yIn ,):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(os.path.join('images', fileName))
        self.image = pygame.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (xIn,yIn)
        self.WIDTH = 800
        self.HEIGHT = 600
        self.SPEED = 10
        self.x_speed = 0
        self.y_speed = 0


    def update(self):
        #self.x_speed = 0
        #self.y_speed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.x_speed = -self.SPEED
        if keystate[pygame.K_RIGHT]:
            self.x_speed = self.SPEED
        if keystate[pygame.K_UP]:
            self.y_speed = -self.SPEED
        if keystate[pygame.K_DOWN]:
            self.y_speed = self.SPEED
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

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
