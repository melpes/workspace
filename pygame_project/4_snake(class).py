import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

pygame.init()
pygame.key.set_repeat(5, 5)
surface = pygame.display.set_mode((600, 600))
fpsclock = pygame.time.Clock()

class Snake:
    def __init__(self, pos):
        self.bodies = [pos]

    def move(self, key):
        xpos, ypos = self.bodies[0]
        