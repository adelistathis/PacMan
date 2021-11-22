import pygame
import os
import sys
from Ghost import Ghost
from Wall import Wall
from Block import Block
from Player import Player
from Heart import Heart
import Pacman

pygame.init()

BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(128, 128, 128)
RED = pygame.Color(255, 0, 0)
ORANGE = pygame.Color(255, 165, 0)

# instantiate the Player() and Ghost() objects
pac = Player(fileName='pacman_o.png', xIn=30, yIn=30, lives=3)
inky = Ghost(fileName='inky.png', x=285, y=75)
blinky = Ghost(fileName='blinky.png', x=285, y=75)
pinky = Ghost(fileName='pinky.png', x=285, y=195)
clyde = Ghost(fileName='clyde.png', x=285, y=195)

all_sprites_list = pygame.sprite.RenderPlain()
all_sprites_list.add(pac)

# Add the ghosts to the ghost list and list of all the sprites
ghost_list = pygame.sprite.RenderPlain()
ghost_list.add(inky)
ghost_list.add(blinky)
ghost_list.add(pinky)
ghost_list.add(clyde)
all_sprites_list.add(ghost_list)

# Create the walls
wall_list = Pacman.setup_room()
all_sprites_list.add(wall_list)

# Create the blocks
block_list = Pacman.create_blocks(wall_list, all_sprites_list)
all_sprites_list.add(block_list)

# Instantiate the hearts and add them to the heart list
heart_1 = Heart(fileName='heart.jpeg', xIn=20, yIn=625)
heart_2 = Heart(fileName='heart.jpeg', xIn=60, yIn=625)
heart_3 = Heart(fileName='heart.jpeg', xIn=100, yIn=625)

# Add the hearts to the heart list and list of all the sprites
heart_list = pygame.sprite.RenderPlain()
heart_list.add(heart_1)
heart_list.add(heart_2)
heart_list.add(heart_3)
all_sprites_list.add(heart_list)

clock = pygame.time.Clock()
count = 0
running = True

(width, height) = (606, 650)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PacMan")

died = False
iterations_after_death = 0

while running:
    count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ghosts
    inky.move(wall_list)
    blinky.move(wall_list)
    pinky.move(wall_list)
    clyde.move(wall_list)

    # Move pacman
    pac.update(wall_list)

    # Give PacMan the ability to eat blocks
    pac.eat_block(block_list)

    # check if pac died
    if pac.die(ghost_list): # will run the function in order to check the if-statement
        Pacman.remove_heart(heart_list)

    # fill the background
    screen.fill(BLACK)

    # Draw the sprites
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(100)