import pygame
from Wall import Wall
from Block import Block

pygame.init()

BLUE = pygame.Color(0, 0, 255)
ORANGE = pygame.Color(255, 165, 0)


def setup_room():
    """ creates all of the walls in the game maze

    :return: a list containing all of the Wall objects in the game
    """

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
             [240, 240, 6, 66],
             [240, 300, 126, 6],
             [240, 240, 35, 6],
             [331, 240, 35, 6],
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

    # return our new list
    return wall_list


def create_blocks(wall_list):
    """creates all of the consumable blocks in the game

    :param wall_list: a list containing all of the Wall objects in the game
    :return: a list containing all of the Block objects in the game
    """
    block_list = pygame.sprite.RenderPlain()

    for row in range(19):
        for column in range(19):

            # prevents blocks from being created on rows 7 and 8 and columns 8, 9, and 10
            if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
                continue
            else:
                block = Block(ORANGE, 4, 4)

                # set the x and y coordinates of the upper left corner of the block
                block.rect.x = (30 * column + 6) + 26
                block.rect.y = (30 * row + 6) + 26

                b_collide = pygame.sprite.spritecollide(block, wall_list, False)

                # does not add the block to the block_list if it collides with a Wall object
                if b_collide:
                    continue
                else:
                    block_list.add(block)

    return block_list


def remove_life(life_list):
    """Removes one of the player's lives (called after the player dies in-game)

    :param life_list: a list containing all of the player's Life objects
    """
    life_list.sprites()[len(life_list.sprites()) - 1].kill()









