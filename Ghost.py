import random
import os
import pygame


class Ghost(pygame.sprite.Sprite):

    def __init__(self, fileName, x, y):

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load(os.path.join('images', fileName))
        self.image = pygame.transform.scale(image, (40, 40))

        self.rect = self.image.get_rect()
        self.rect.left = x # position of left side of sprite's rectangle
        self.rect.top = y # position of top of sprite's rectangle
        self.direction = "UP"
        self.SPEED = 3 # used to change the values of "x_speed" and "y_speed"
        self.WIDTH = 606 # width of window
        self.HEIGHT = 606 # height of window
        self.x_speed = 0 # how many pixels the sprite moves in the x-direction (per move)
        self.y_speed = 0 # how many pixels the sprite moves in the y-direction (per move)

    def choose_direction(self):
        """Chooses a random direction for the Ghost() object to move in

        :return: a String that represents which direction the Ghost() object is to move in
        """
        a = random.randint(1, 4)

        # Assigns a direction to each possible value of "a"
        if a == 1:
            return "UP"
        elif a == 2:
            return "DOWN"
        elif a == 3:
            return "LEFT"
        elif a == 4:
            return "RIGHT"

    def move(self, wall_list, name):
        """Moves the Ghost() objects by randomizing their direction and changing it if they collide with a Wall() object

        :param wall_list: a Group containing all of the Wall() sprites in the game
        :param name: the variable name of the Ghost sprite
        """

        # change x_speed and y_speed based on which direction the ghost is set to move in
        if self.direction == "LEFT":
            image = pygame.image.load(os.path.join('images', '{}_left.png'.format(name)))
            self.image = pygame.transform.scale(image, (40, 40))
            self.x_speed = -self.SPEED
            self.y_speed = 0
        elif self.direction == "RIGHT":
            image = pygame.image.load(os.path.join('images', '{}_right.png'.format(name)))
            self.image = pygame.transform.scale(image, (40, 40))
            self.x_speed = self.SPEED
            self.y_speed = 0
        elif self.direction == "UP":
            self.y_speed = -self.SPEED
            self.x_speed = 0
        elif self.direction == "DOWN":
            self.y_speed = self.SPEED
            self.x_speed = 0

        # move the ghosts
        self.rect.left += self.x_speed
        self.rect.top += self.y_speed

        # make sure that the ghosts cannot move off of the screen
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

        # collision detection
        collision = pygame.sprite.spritecollide(self, wall_list, False)

        # if there is a collision
        if collision:
            self.rect.x += -self.x_speed # move the sprite's rectangle back to its previous horizontal position
            self.rect.y += -self.y_speed # move the sprite's rectangle back to its previous vertical position
            self.x_speed = 0
            self.y_speed = 0
            self.direction = self.choose_direction() # randomize the direction again

































