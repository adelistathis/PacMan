import sys

import pygame
from pygame.locals import *

pygame.init()

FPS = 30
FramePerSec = pygame.time.Clock() # create a clock object to keep track of time

# Setting up color objects (RGB color system)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(128, 128, 128)
red = pygame.Color(255, 0, 0)

# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((300, 300))
DISPLAYSURF.fill(white)
pygame.display.set_caption("Example Code")

# Creating Lines and Shapes
pygame.draw.line(DISPLAYSURF, blue, (150, 130), (130, 170)) # draws a blue line from (150, 130) to (130, 170)
pygame.draw.line(DISPLAYSURF, blue, (150, 130), (170, 170)) # draws a blue line from (150, 130) to (170, 170)
pygame.draw.line(DISPLAYSURF, green, (130, 170), (170, 170)) # draws a green line from (130, 170) to (170, 170)
pygame.draw.circle(DISPLAYSURF, black, (100, 50), 30) # draws a black-FILLED circle centered at (100, 50) with radius 30 pixels
pygame.draw.circle(DISPLAYSURF, black, (200, 50), 30) # draws a black-FILLED circle centered at (200, 50) with radius 30 pixels

# draws a red-BORDERED rectangle with upper left corner at (100, 200), width 100 pixels, and height 50 pixels
pygame.draw.rect(DISPLAYSURF, red, (100, 200, 100, 50), 2) # the 2 makes it so that the border is red (the rectangle is NOT filled)

# draws a black-FILLED rectangle with upper left corner at (110, 260), width 80 pixels, and height 10 pixels
pygame.draw.rect(DISPLAYSURF, black, (110, 260, 80, 10))


# GAME LOOP
while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    FramePerSec.tick(FPS) # makes the clock tick
