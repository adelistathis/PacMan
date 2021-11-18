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

x = 285
y = 200

pac = Player('pacman_o.png', 30, 30)
inky = Ghost('inky.png', x, y)
blinky = Ghost('blinky.png', x, y)
pinky = Ghost('pinky.png', x, y)
clyde = Ghost('clyde.png', x, y)

all_sprites_list = pygame.sprite.RenderPlain()
all_sprites_list.add(pac)

ghost_list = pygame.sprite.RenderPlain()
ghost_list.add(inky)
ghost_list.add(blinky)
ghost_list.add(pinky)
ghost_list.add(clyde)
all_sprites_list.add(ghost_list)

clock = pygame.time.Clock()
count = 0
running = True

(width, height) = (606, 606)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PacMan")
wall_list = Pacman.setup_room()
block_list = Pacman.create_blocks(wall_list, all_sprites_list)

while running:
    count += 1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    # Move the ghosts
    inky.move(wall_list, count)
    blinky.move(wall_list, count)
    pinky.move(wall_list, count)
    clyde.move(wall_list, count)
    # move pacman
    pac.update()


    screen.fill(BLACK)


    # Draw the everything
    all_sprites_list.draw(screen)

    wall_list.draw(screen)
    block_list.draw(screen)





    pygame.display.flip()
