import pygame

n = 0
clock = pygame.time.Clock()

def average_fps(average_fps):
    global n
    if n == 0:
        pass
    else:
        average_fps = average_fps * (n / (n + 1)) * (n * average_fps + clock.get_fps()) / (n * average_fps)
    n += 1
    return average_fps