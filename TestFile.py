import pygame
import os
import sys
from Ghost import Ghost
from Wall import Wall
from Block import Block
from Player import Player
import Pacman

pygame.init()

BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(128, 128, 128)
RED = pygame.Color(255, 0, 0)
ORANGE = pygame.Color(255, 165, 0)


pac = Player('pacman_o.png', 30, 30)
inky = Ghost('inky.png', 285, 75)
blinky = Ghost('blinky.png', 285, 75)
pinky = Ghost('pinky.png', 285, 195)
clyde = Ghost('clyde.png', 285, 195)

all_sprites_list = pygame.sprite.RenderPlain()
all_sprites_list.add(pac)

# Create the ghosts
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

clock = pygame.time.Clock()
count = 0
running = True

(width, height) = (606, 606)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PacMan")

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

    screen.fill(BLACK)

    # Draw the sprites
    wall_list.draw(screen)
    block_list.draw(screen)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(120)