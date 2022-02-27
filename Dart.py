import pygame
import os
import math

WIDTH, HEIGHT = 50, 50
SPEED = 15


class Dart():

    def __init__(self, x, y, xdir, ydir):
        self.width = WIDTH
        self.height = HEIGHT
        # self.active = False
        self.x, self.y = x, y
        self.xdir, self.ydir = xdir, ydir
        self.xvel = xdir * SPEED
        self.yvel = ydir * SPEED

        self.image = pygame.image.load(
            os.path.join('image', 'dart.jpg'))

    def move(self):
        self.x += self.xvel
        self.y += self.yvel
