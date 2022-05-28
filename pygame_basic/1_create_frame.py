import pygame
pygame.init()

screen_width = 1280
screen_height= 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("LAC Game")

running = True

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

pygame.quit()