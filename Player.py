import sys
import pygame
import os
from Block import Block


ORANGE = pygame.Color(255, 165, 0)


def create_blocks(wall_list):
    block_list = pygame.sprite.RenderPlain()

    # Draw the grid
    for row in range(19):
        for column in range(19):
            if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
                continue
            else:
                block = Block(ORANGE, 4, 4)

                # Set a random location for the block
                block.rect.x = (30 * column + 6) + 26
                block.rect.y = (30 * row + 6) + 26

                b_collide = pygame.sprite.spritecollide(block, wall_list, False)
                if b_collide:
                    continue
                else:
                    # Add the block to the list of objects
                    block_list.add(block)

    return block_list


class Player(pygame.sprite.Sprite):
    def __init__(self, fileName, xIn, yIn, lives):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(os.path.join('images', fileName))
        self.ogImage = pygame.transform.scale(image, (35, 35))
        self.image = self.ogImage
        self.rect = self.image.get_rect()
        self.rect.center = (xIn, yIn)
        self.WIDTH = 606 # width of game window
        self.HEIGHT = 606 # height of game window
        self.SPEED = 2 # number of pixels PacMan moves in each move
        self.x_speed = 0
        self.y_speed = 0
        self.score = 0
        self.leftImage = pygame.transform.flip(self.ogImage, True, False)
        self.downImage = pygame.transform.rotate(self.ogImage, 270)
        self.upImage = pygame.transform.rotate(self.ogImage, 90)
        self.lives = lives

    def update(self, wall_list):
        """Gives the player key controls to move their sprite

        Also handles collisions with walls

        :param wall_list: a Group containing all of the Wall() sprites in the game
        """

        keystate = pygame.key.get_pressed()

        # changes x and y speeds depending on which key was pressed by the Player
        if keystate[pygame.K_LEFT]:
            self.x_speed = -self.SPEED
            self.y_speed = 0
        elif keystate[pygame.K_RIGHT]:
            self.x_speed = self.SPEED
            self.y_speed = 0
        elif keystate[pygame.K_UP]:
            self.y_speed = -self.SPEED
            self.x_speed = 0
        elif keystate[pygame.K_DOWN]:
            self.y_speed = self.SPEED
            self.x_speed = 0


        # prevents the Player() object from moving off screen
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH
            # self.x_speed = 0
        if self.rect.left < 0:
            self.rect.left = 0
            # self.x_speed = 0
        if self.rect.top < 0:
            self.rect.top = 0
            # self.y_speed = 0
        if self.rect.bottom > self.HEIGHT:
            self.rect.bottom = self.HEIGHT
            # self.y_speed = 0

        self.leftImage = pygame.transform.flip(self.image,True, False)
        self.downImage = pygame.transform.rotate(self.image, 270)
        self.upImage = pygame.transform.rotate(self.image, 90)

        if self.x_speed < 0:
            self.image = self.leftImage
        if self.y_speed < 0:
            self.image = self.downImage
        if self.y_speed > 0 :
            self.image = self.upImage
        if self.x_speed > 0 :
            self.image = self.ogImage

        # move the Player() object
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        hits = pygame.sprite.spritecollide(self, wall_list, False)
        # if there was a collision between the Player() object and a Wall() object
        if hits:
            self.rect.x += -self.x_speed
            self.rect.y += -self.y_speed
            self.x_speed = 0
            self.y_speed = 0

    def eat_block(self, block_list, wall_list, all_sprites_list):
        """Gives the player the ability to eat Block() sprites

        :param block_list: a Group containing all of the Block() sprites in the game
        """

        collision = pygame.sprite.spritecollide(self, block_list, False)

        # traverses the list of blocks that the Player() collided with
        for collided in collision:
            collided.kill()
            self.score += 1

        # if self.score != 0 and self.score % 210 == 0:
        #     block_list = create_blocks(wall_list) # add the blocks to the block_list again
        #     all_sprites_list.add(block_list)
        #     self.score += 10

    def die(self, ghost_list):
        """'kills' the Player() object if they collide with a ghost by reducing their # of lives and redrawing them
        on the screen

        exits the game if the player has lost all of their lives

        :param ghost_list: a Group containing all of the Ghost() sprites in the game
        """

        # check for a collision between PacMan and the ghosts
        collision = pygame.sprite.spritecollide(self, ghost_list, False)

        if len(collision) > 0:
            self.lives -= 1

            if self.lives == 0:
                pygame.quit()
                sys.exit()

            # Move the Player to their original position
            self.rect.center = (303, 280)

            return True

        return False







