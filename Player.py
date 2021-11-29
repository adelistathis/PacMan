import sys
import pygame
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, fileName, xIn, yIn, lives):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(os.path.join('images', fileName))
        self.ogImage = pygame.transform.scale(image, (37, 37))
        self.image = self.ogImage.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (xIn, yIn)
        self.WIDTH = 606 # width of game window
        self.HEIGHT = 606 # height of game window
        self.SPEED = 2 # number of pixels PacMan moves in each move
        self.x_speed = 0
        self.y_speed = 0
        self.score = 0
        self.leftImage = pygame.transform.flip(self.ogImage.copy(), True, False)
        self.downImage = pygame.transform.rotate(self.ogImage.copy(), 90)
        self.upImage = pygame.transform.rotate(self.ogImage.copy(), 270)
        self.direction = 0
        self.lives = lives

    def update(self, wall_list):
        """Gives the player key controls to move their sprite

        Also handles collisions with walls

        :param wall_list: a Group containing all of the Wall() sprites in the game
        """

        if self.x_speed < 0:
            self.direction = 2
        if self.y_speed < 0:
            self.direction = 3
        if self.y_speed > 0 :
            self.direction = 1
        if self.x_speed > 0 :
            self.direction = 0
        if self.x_speed == 0 and self.y_speed == 0:
            self.direction = 5
        keystate = pygame.key.get_pressed()

        # changes x and y speeds depending on which key was pressed by the Player
        if keystate[pygame.K_LEFT] and self.direction != 0:
            self.x_speed = -self.SPEED
            self.y_speed = 0
        elif keystate[pygame.K_RIGHT] and self.direction != 2:
            self.x_speed = self.SPEED
            self.y_speed = 0
        elif keystate[pygame.K_UP] and self.direction != 1:
            self.y_speed = -self.SPEED
            self.x_speed = 0
        elif keystate[pygame.K_DOWN] and self.direction != 3:
            self.y_speed = self.SPEED
            self.x_speed = 0


        # prevents the Player() object from moving off screen
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH
            self.x_speed = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.x_speed = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.y_speed = 0
        if self.rect.bottom > self.HEIGHT:
            self.rect.bottom = self.HEIGHT
            self.y_speed = 0




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



        if self.x_speed < 0:
            self.image = self.leftImage.copy()
        if self.y_speed < 0:
            self.image = self.downImage.copy()
        if self.y_speed > 0 :
            self.image = self.upImage.copy()
        if self.x_speed > 0 :
            self.image = self.ogImage.copy()



    def eat_block(self, block_list):
        """Gives the player the ability to eat Block() sprites

        :param block_list: a Group containing all of the Block() sprites in the game
        """

        collision = pygame.sprite.spritecollide(self, block_list, False)

        # traverses the list of blocks that the Player() collided with
        for collided in collision:
            collided.kill()
            self.score += 1

        # If the player's score equals the number of blocks on the board
        if self.score == 210:
            pygame.quit()
            sys.exit()

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
            self.rect.x = 15
            self.rect.y = 15

            return True

        return False







