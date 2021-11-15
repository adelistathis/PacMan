import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

blue  = (0, 0, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((400,600)) # creates a 400-by-600 window
DISPLAYSURF.fill(white) # makes the screen background white
pygame.display.set_caption("Game") # the caption of the game


class Enemy(pygame.sprite.Sprite): # child class of the Sprite class
    def __init__(self):
        super().__init__() # calls the super-constructor
        self.image = pygame.image.load("enemy.png") # loads an image of the enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 400 - 40), 0) # defines the center of the enemy's rectangle

    def move(self):
        self.rect.move_ip(0, 10) # moves the Enemy Sprite 10 pixels down
        if (self.rect.bottom > 600): # checks to see if the enemy has reached the bottom of the screen
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0) # randomizes center at an x-coordinate at the top of the window

    def draw(self, surface):
        surface.blit(self.image, self.rect) # used to draw a surface onto another
        # first parameter is image to be drawn to, second parameter is the object


class Player(pygame.sprite.Sprite): # child class of the Sprite class
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png") # loads an image of the player
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) # defines the center of the player's rectangle

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        #
        # if pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0,5)

        # checks to make sure the player's rectangle is in the window
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0) # moves the rectangle 5 pixels to the left

        # checks to make sure the player's rectangle is in the window
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0) # moves the rectangle 5 pixels to the right

    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player()
E1 = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()

    DISPLAYSURF.fill(white)
    # P1.draw(DISPLAYSURF)
    # E1.draw(DISPLAYSURF)

    pygame.display.update() # updates the screen with all of the commands that have occurred up to that point
    FramePerSec.tick(FPS) # makes sure it only repeats "FPS" times per second