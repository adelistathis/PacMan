import sys
import pygame
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, xIn, yIn, lives):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(os.path.join('images', "pacman_right.png"))
        self.image = pygame.transform.scale(image, (37, 37))
        self.rect = self.image.get_rect()
        self.rect.center = (xIn, yIn)
        self.WIDTH = 606 # width of game window
        self.HEIGHT = 606 # height of game window
        self.SPEED = 3 # number of pixels PacMan moves in each move
        self.x_speed = 0
        self.y_speed = 0
        self.score = 0
        self.rightImage = pygame.image.load(os.path.join('images', "pacman_right.png"))
        self.rightImage = pygame.transform.scale(self.rightImage, (37, 37))
        self.leftImage = pygame.image.load(os.path.join('images', "pacman_left.png"))
        self.leftImage = pygame.transform.scale(self.leftImage, (37, 37))
        self.downImage = pygame.image.load(os.path.join('images', "pacman_down.png"))
        self.downImage = pygame.transform.scale(self.downImage, (37, 37))
        self.upImage = pygame.image.load(os.path.join('images', "pacman_up.png"))
        self.upImage = pygame.transform.scale(self.upImage, (37, 37))
        self.lives = lives

    def update(self, wall_list):
        """Gives the player key controls to move their sprite

        Also handles collisions with walls

        :param wall_list: a Group containing all of the Wall() sprites in the game
        """

        keystate = pygame.key.get_pressed()

        # changes x and y speeds depending on which key was pressed by the Player
        if (keystate[pygame.K_a] or keystate[pygame.K_LEFT]) and self.x_speed <= 0:
            self.x_speed = -self.SPEED
            self.y_speed = 0
        elif (keystate[pygame.K_d] or keystate[pygame.K_RIGHT]) and self.x_speed >= 0:
            self.x_speed = self.SPEED
            self.y_speed = 0
        elif (keystate[pygame.K_w] or keystate[pygame.K_UP]) and self.y_speed <= 0:
            self.y_speed = -self.SPEED
            self.x_speed = 0
        elif (keystate[pygame.K_s] or keystate[pygame.K_DOWN]) and self.y_speed >= 0:
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

        #handles wall collisions
        hits = pygame.sprite.spritecollide(self, wall_list, False)
        # if there was a collision between the Player() object and a Wall() object
        if hits:
            self.rect.x += -self.x_speed
            self.rect.y += -self.y_speed
            self.x_speed = 0
            self.y_speed = 0

        # makes pacman face the right way
        if self.x_speed < 0:
            self.image = self.leftImage.copy()
        if self.y_speed < 0:
            self.image = self.upImage.copy()
        if self.y_speed > 0 :
            self.image = self.downImage.copy()
        if self.x_speed > 0 :
            self.image = self.rightImage.copy()

    def eat_block(self, frames , block_list):
        """Gives the player the ability to eat Block() sprites

        :param block_list: a Group containing all of the Block() sprites in the game
        """

        collision = pygame.sprite.spritecollide(self, block_list, False)

        s = 'sounds'
        chomp = pygame.mixer.Sound(os.path.join(s, 'chomp.wav'))

        # traverses the list of blocks that the Player() collided with
        for collided in collision:
            if(frames > 30):
                pygame.mixer.Sound.play(chomp)
                frames = 0

            collided.kill()
            self.score += 1

        # If the player's score equals the number of blocks on the board
        if self.score == 210:
            pass
        return frames

    def die(self, ghost_list):
        gameOver=False
        """'kills' the Player() object if they collide with a ghost by reducing their # of lives and redrawing them
        on the screen

        exits the game if the player has lost all of their lives

        :param ghost_list: a Group containing all of the Ghost() sprites in the game
        """

        # check for a collision between PacMan and the ghosts
        collision = pygame.sprite.spritecollide(self, ghost_list, False)

        # load the death sound
        s = 'sounds'
        death = pygame.mixer.Sound(os.path.join(s, 'death.wav'))

        if len(collision) > 0:
            pygame.mixer.Sound.play(death)
            self.lives -= 1
            self.x_speed = 0
            self.y_speed = 0

            if self.lives == 0:
                gameOver = True

            # Move the Player to their original position
            self.rect.centerx = 303
            self.rect.centery = 275

            return (True,gameOver)

        return (False,gameOver)







