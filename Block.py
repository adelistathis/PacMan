import pygame.sprite


WHITE = pygame.Color(255, 255, 255)
ORANGE = pygame.Color(255, 165, 0)

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(ORANGE)
        self.image.set_colorkey(ORANGE)
        pygame.draw.rect(self.image, self.image.color)