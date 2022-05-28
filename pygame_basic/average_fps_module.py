import pygame

clock = pygame.time.Clock()

def average_fps(average_fps, n):
    if n == 0:
        pass
    else:
        average_fps = ( average_fps * n + clock.get_fps() ) / (n + 1)
    n += 1
    return average_fps, n