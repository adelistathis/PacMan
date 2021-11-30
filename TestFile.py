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
framesSinceSound = 0

# instantiate the Player() and Ghost() objects
# pac = Player(xIn=30, yIn=30, lives=3)
# inky = Ghost(fileName='inky.png', x=285, y=75)
# blinky = Ghost(fileName='blinky.png', x=285, y=75)
# pinky = Ghost(fileName='pinky.png', x=285, y=75)
# clyde = Ghost(fileName='clyde.png', x=285, y=195)
# drinky = Ghost(fileName='drinky.png', x=285, y=195)





# instantiate the Ghost() objects
inky = Ghost(fileName='inky_right.png', x=285, y=75)
blinky = Ghost(fileName='blinky_right.png', x=285, y=75)
pinky = Ghost(fileName='pinky_right.png', x=285, y=380)
clyde = Ghost(fileName='clyde_right.png', x=285, y=380)
# drinky = Ghost(fileName='drinky_right.png', x=285, y=195) <-- FIFTH ghost




# Instantiate the hearts and add them to the heart list
life_1 = Life(fileName='life.jpeg', xIn=20, yIn=625)
life_2 = Life(fileName='life.jpeg', xIn=60, yIn=625)
life_3 = Life(fileName='life.jpeg', xIn=100, yIn=625)

# Add the hearts to the heart list and list of all the sprites


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
pygame.mixer.set_num_channels(2)


game_over = True

def show_go_screen():

    screen.fill(BLACK)
    font = pygame.font.SysFont('Comic Sans MS', 90)  # Text font
    gameOverText = font.render("PACMAN", False, YELLOW)
    gameOverTextRect = gameOverText.get_rect()
    gameOverTextRect.center = (width/2,height/2 - 40)
    screen.blit(gameOverText,(gameOverTextRect.x,gameOverTextRect.y))

    font = pygame.font.SysFont('Comic Sans MS', 30)
    playAgainText = font.render("press any key to play", False, BLUE)
    playAgainTextRect = playAgainText.get_rect()
    playAgainTextRect.center = (width / 2, height / 2 + 20)
    screen.blit(playAgainText, (playAgainTextRect.x, playAgainTextRect.y))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False




while running:
    if game_over:
        show_go_screen()
        game_over = False
        pygame.mixer.Sound.play(intro)

        #init sprite list
        all_sprites_list = pygame.sprite.RenderPlain()

        # Create the walls
        wall_list = Pacman.setup_room()
        all_sprites_list.add(wall_list)

        # Create the blocks
        block_list = Pacman.create_blocks(wall_list)
        all_sprites_list.add(block_list)

        # instantiate the Player() object and add it to the all_sprite list
        pac = Player(xIn=303, yIn=275, lives=3)
        all_sprites_list.add(pac)

        #add lives
        life_list = pygame.sprite.RenderPlain()
        life_list.add(life_1)
        life_list.add(life_2)
        life_list.add(life_3)
        all_sprites_list.add(life_list)
        # Add the ghosts to the ghost list and list of all the sprites
        ghost_list = pygame.sprite.RenderPlain()
        ghost_list.add(inky)
        ghost_list.add(blinky)
        ghost_list.add(pinky)
        ghost_list.add(clyde)
        #ghost_list.add(drinky)
        all_sprites_list.add(ghost_list)

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
    framesSinceSound = pac.eat_block(framesSinceSound, block_list)

    # checks if all of the blocks in the maze have been eaten
    if len(block_list) == 0:
        game_over = True

    # check if pac died
    if pac.die(ghost_list): # will run the function in order to check the if-statement
        Pacman.remove_life(life_list)
    if not pac.hasLives():
        game_over = True


    # fill the background
    screen.fill(BLACK)

    # Draw the sprites
    all_sprites_list.draw(screen)
    text = font.render("SCORE: {}".format(pac.score), False, YELLOW)
    screen.blit(text, (460, 620))

    pygame.display.flip()

    framesSinceSound += 1

    clock.tick(60)