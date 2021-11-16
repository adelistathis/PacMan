import pygame
import os
import sys
from Ghost import Ghost
from Wall import Wall
from Block import Block
from Player import Player

pygame.init()


def setup_gate(all_sprites_list):
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(282, 242, 42, 2, WHITE))
    all_sprites_list.add(gate)
    return gate

def draw_window():
    WIN.fill(BLACK) # "WIN" stands for window
    WIN.blit(PACMAN1, (300,100))
    WIN.blit(PACMAN2, (600, 100))
    WIN.blit(PACMAN3, (300, 300))
    WIN.blit(PACMAN4, (600, 300))
    pygame.display.update()



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

WIDTH, HEIGHT = 500, 500
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









