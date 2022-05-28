import pygame

clock = pygame.time.Clock()

def average_fps(average_fps, n, newfps):
    if clock.get_fps() != 0:
        average_fps = ( average_fps * n + newfps ) / (n + 1)
    n += 1
    return average_fps, n