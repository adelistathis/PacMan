import pygame
import os
import sys
from Ghost import Ghost
from Wall import Wall
from Block import Block
from Player import Player
from Life import Life
import Pacman

pygame.init()

BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(128, 128, 128)
RED = pygame.Color(255, 0, 0)
ORANGE = pygame.Color(255, 165, 0)
YELLOW = (255, 255, 0)

# instantiate the Player() and Ghost() objects
#pac = Player(xIn=30, yIn=30, lives=3)
#inky = Ghost(fileName='inky.png', x=285, y=75)
#blinky = Ghost(fileName='blinky.png', x=285, y=75)
#pinky = Ghost(fileName='pinky.png', x=285, y=75)
#clyde = Ghost(fileName='clyde.png', x=285, y=195)
#drinky = Ghost(fileName='drinky.png', x=285, y=195)

all_sprites_list = pygame.sprite.RenderPlain()

# Create the walls
wall_list = Pacman.setup_room()
all_sprites_list.add(wall_list)

# Create the blocks
block_list = Pacman.create_blocks(wall_list)
all_sprites_list.add(block_list)

# instantiate the Player() object and add it to the all_sprite list
pac = Player( xIn=303, yIn=275, lives=3)
all_sprites_list.add(pac)

# instantiate the Ghost() objects
inky = Ghost(fileName='inky_right.png', x=285, y=75)
blinky = Ghost(fileName='blinky_right.png', x=285, y=75)
pinky = Ghost(fileName='pinky_right.png', x=285, y=380)
clyde = Ghost(fileName='clyde_right.png', x=285, y=380)
# drinky = Ghost(fileName='drinky_right.png', x=285, y=195) <-- FIFTH ghost


# Add the ghosts to the ghost list and list of all the sprites
ghost_list = pygame.sprite.RenderPlain()
ghost_list.add(inky)
ghost_list.add(blinky)
ghost_list.add(pinky)
ghost_list.add(clyde)
# ghost_list.add(drinky)
all_sprites_list.add(ghost_list)

# Instantiate the hearts and add them to the heart list
life_1 = Life(fileName='life.jpeg', xIn=20, yIn=625)
life_2 = Life(fileName='life.jpeg', xIn=60, yIn=625)
life_3 = Life(fileName='life.jpeg', xIn=100, yIn=625)

# Add the hearts to the heart list and list of all the sprites
life_list = pygame.sprite.RenderPlain()
life_list.add(life_1)
life_list.add(life_2)
life_list.add(life_3)
all_sprites_list.add(life_list)

clock = pygame.time.Clock()
count = 0
running = True

(width, height) = (606, 650)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PacMan")

font = pygame.font.SysFont('Comic Sans MS', 30) # Text font

text = font.render("SCORE: ", False, YELLOW)
textRect = text.get_rect()
textRect.center = (580, 625)


s = 'sounds'
intro = pygame.mixer.Sound(os.path.join(s, 'intro.wav'))
pygame.mixer.Sound.play(intro)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ghosts
    inky.move(wall_list, name='inky')
    blinky.move(wall_list, name='blinky')
    pinky.move(wall_list, name='pinky')
    clyde.move(wall_list, name='clyde')
    # drinky.move(wall_list)

    # Move pacman
    pac.update(wall_list)

    # Give PacMan the ability to eat blocks
    pac.eat_block(block_list)

    # checks if all of the blocks in the maze have been eaten
    if len(block_list) == 0:
        block_list = Pacman.create_blocks(wall_list) # 'respawns' the blocks

        # remove the ghosts so that they aren't behind the blocks when the blocks are redrawn on the screen
        all_sprites_list.remove(inky)
        all_sprites_list.remove(blinky)
        all_sprites_list.remove(pinky)
        all_sprites_list.remove(clyde)

        # add the block list to the list of all the sprites in the game
        all_sprites_list.add(block_list)
        # add the ghost list back
        all_sprites_list.add(ghost_list)

        # play the intro music again
        pygame.mixer.Sound.play(intro)

    # check if pac died
    if pac.die(ghost_list): # will run the function in order to check the if-statement
        Pacman.remove_life(life_list)

    # fill the background
    screen.fill(BLACK)

    # Draw the sprites
    all_sprites_list.draw(screen)
    text = font.render("SCORE: {}".format(pac.score), False, YELLOW)
    screen.blit(text, (460, 620))

    pygame.display.flip()
    clock.tick(60)