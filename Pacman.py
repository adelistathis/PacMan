import pygame
import os
import sys
from Ghost import Ghost
from Wall import Wall
from Block import Block
from Player import Player

pygame.init()


def draw_window():
    WIN.fill(BLACK) # "WIN" stands for window
    WIN.blit(PACMAN1, (300,100))
    WIN.blit(PACMAN2, (600, 100))
    WIN.blit(PACMAN3, (300, 300))
    WIN.blit(PACMAN4, (600, 300))
    pygame.display.update()


# This creates all the walls in room 1
def setup_room(all_sprites_list):
    # Make the walls. (x_pos, y_pos, width, height)
    wall_list = pygame.sprite.RenderPlain()

    # This is a list of walls. Each is in the form [x, y, width, height]
    walls = [[0, 0, 6, 600],
             [0, 0, 600, 6],
             [0, 600, 606, 6],
             [600, 0, 6, 606],
             [300, 0, 6, 66],
             [60, 60, 186, 6],
             [360, 60, 186, 6],
             [60, 120, 66, 6],
             [60, 120, 6, 126],
             [180, 120, 246, 6],
             [300, 120, 6, 66],
             [480, 120, 66, 6],
             [540, 120, 6, 126],
             [120, 180, 126, 6],
             [120, 180, 6, 126],
             [360, 180, 126, 6],
             [480, 180, 6, 126],
             [180, 240, 6, 126],
             [180, 360, 246, 6],
             [420, 240, 6, 126],
             [240, 240, 42, 6],
             [324, 240, 42, 6],
             [240, 240, 6, 66],
             [240, 300, 126, 6],
             [360, 240, 6, 66],
             [0, 300, 66, 6],
             [540, 300, 66, 6],
             [60, 360, 66, 6],
             [60, 360, 6, 186],
             [480, 360, 66, 6],
             [540, 360, 6, 186],
             [120, 420, 366, 6],
             [120, 420, 6, 66],
             [480, 420, 6, 66],
             [180, 480, 246, 6],
             [300, 480, 6, 66],
             [120, 540, 126, 6],
             [360, 540, 126, 6]
             ]

    # Loop through the list. Create the wall, add it to the list
    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], BLUE)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    # return our new list
    return wall_list


def setup_gate(all_sprites_list):
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(282, 242, 42, 2, WHITE))
    all_sprites_list.add(gate)
    return gate


def start_game():

    all_sprites_list = pygame.sprite.RenderPlain()

    block_list = pygame.sprite.RenderPlain()

    monster_list = pygame.sprite.RenderPlain()

    pacman_collide = pygame.sprite.RenderPlain()

    wall_list = setup_room(all_sprites_list)

    gate = setup_gate(all_sprites_list)


BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(128, 128, 128)
RED = pygame.Color(255, 0, 0)

FPS = 120

PACMAN1_ = pygame.image.load(os.path.join('images','pacman_c.png'))
PACMAN1 = pygame.transform.scale(PACMAN1_,(100,100))

PACMAN2_ = pygame.image.load(os.path.join('images','pacman_cr.png'))
PACMAN2 = pygame.transform.scale(PACMAN2_,(100,100))

PACMAN3_ = pygame.image.load(os.path.join('images','pacman_o.png'))
PACMAN3 = pygame.transform.scale(PACMAN3_,(100,100))

PACMAN4_ = pygame.image.load(os.path.join('images','pacman_or.png'))
PACMAN4 = pygame.transform.scale(PACMAN4_,(100,100))


WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PacMan")

# Create a surface we can draw on
background = pygame.Surface((500, 500))
background.fill(BLACK)

# default locations for Pacman and monstas
w = 303-16 # Width
p_h = (7*60)+19 # Pacman height
m_h = (4*60)+19 # Monster height
b_h = (3*60)+19 # Binky height
i_w = 303-16-32 # Inky width
c_w = 303+(32-16) # Clyde width

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 24)


start_game()

pygame.quit()
sys.exit()









