import sys
from random import randint
from math import hypot
import pygame
from pygame import rect
from pygame.locals import Rect, QUIT, MOUSEMOTION, MOUSEBUTTONDOWN

class House:
    def __init__(self, xpos) -> None:
        self.rect = Rect(xpos, 550, 40, 40)
        self.exploded = False
        strip = pygame.image.load("")