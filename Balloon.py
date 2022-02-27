import pygame
import os

WIDTH, HEIGHT = 50, 50
VEL = 3


class Balloon():

    def __init__(self, x, y, hits):
        self.width = WIDTH
        self.height = HEIGHT
        self.hits = hits
        self.x, self.y = x, y
        self.image = pygame.image.load(
            os.path.join('image', 'balloon.jpg'))

    def move(self):
        self.x += VEL
