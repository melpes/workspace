import random
import pygame

pygame.init()

background = pygame.display.set_mode((400,300))

fpsclock = pygame.time.Clock()
fps = 30

while True:
    fpsclock.tick(fps)
    background.fill((0, 0, 0))
    point = []
    for _ in range(5):
        xpos = random.randint(0, 400)
        ypos = random.randint(0, 300)
        point.append((xpos, ypos))

    pygame.draw.lines(background, (255, 255, 255), True, point, 5)

    pygame.display.update()