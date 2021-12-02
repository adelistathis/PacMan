import pygame.sprite


class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()