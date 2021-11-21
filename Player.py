import sys

import pygame
import os


# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    def __init__(self, fileName, xIn, yIn):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(os.path.join('images', fileName))
        self.image = pygame.transform.scale(image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.center = (xIn, yIn)
        self.WIDTH = 606
        self.HEIGHT = 606
        self.SPEED = 2
        self.x_speed = 0
        self.y_speed = 0
        self.score = 0
        self.lives = 3

    def update(self, wList):
        hits = pygame.sprite.spritecollide(self, wList, False)


        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.x_speed = -self.SPEED
            self.y_speed = 0
        if keystate[pygame.K_RIGHT]:
            self.x_speed = self.SPEED
            self.y_speed = 0
        if keystate[pygame.K_UP]:
            self.y_speed = -self.SPEED
            self.x_speed = 0
        if keystate[pygame.K_DOWN]:
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
        hits = pygame.sprite.spritecollide(self, wList, False)
        if hits:
            self.rect.x += -self.x_speed
            self.rect.y += -self.y_speed
            self.x_speed = 0
            self.y_speed = 0
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def eat_block(self, block_list):

        collision = pygame.sprite.spritecollide(self, block_list, False)

        for collided in collision:
            collided.kill()
            self.score += 1

    def die(self, ghost_list):

        collision = pygame.sprite.spritecollide(self, ghost_list, False)

        if collision:
            if self.lives == 0:
                pygame.quit()
                sys.exit()

            # Move the Player to their original position
            self.rect.center = (30, 30)
            self.lives -= 1







