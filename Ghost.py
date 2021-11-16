import random
from Wall import Wall

class Ghost():

    def __init__(self, width, height, x, y):
        self.width = width # width of sprite
        self.height = height # height of sprite
        self.x = x # starting x-coordinate (of upper top-left corner)
        self.y = y # starting y-coordinate (of upper top-left corner)

    def move(self):
        speed = 2 # 2 pixels per move

        dx = random.choice([-speed, speed])
        dy = random.choice([-speed, speed])

        self.x += dx
        self.y += dy

    def collision(self):





