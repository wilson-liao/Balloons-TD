from re import X
from tkinter import Y
import pygame
import os
from Dart import Dart
import math

WIDTH, HEIGHT = 100, 100

GRAY = (211, 211, 211, 100)


class Monkey():

    def __init__(self, x, y, radius, damage, WIN):
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = y
        self.image = pygame.image.load(
            os.path.join('image', 'DartMonkey.jpg'))
        self.radius = radius
        self.damage = damage
        self.attackSpeed = 2000  # 2 seconds
        self.WIN = WIN
        self.center = (x - radius + WIDTH//2,
                       y - radius + HEIGHT//2)
        self.lastShotTime = 0

    def draw_radius(self):
        surface = pygame.Surface(
            (self.radius*2, self.radius*2), pygame.SRCALPHA)
        pygame.draw.circle(surface, GRAY,
                           (self.radius, self.radius), self.radius)
        self.WIN.blit(surface, self.center)

    def shoot(self, balloon, curTime):
        if curTime - self.lastShotTime >= self.attackSpeed:

            # Calculating Direction of Dart
            dist = [balloon.x - self.x,
                    balloon.y - self.y]
            norm = math.sqrt(dist[0] ** 2 + dist[1] ** 2)
            dir = [dist[0] / norm, dist[1] / norm]

            self.lastShotTime = curTime
            return Dart(self.x, self.y, dir[0], dir[1])
