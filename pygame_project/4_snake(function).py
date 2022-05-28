import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

pygame.init()
surface = pygame.display.set_mode((600, 600))
fpsclock = pygame.time.Clock()

foods = []
snake = []
(width, height) = (20, 20)

def add_food():
    while True:
        pos = (random.randint(0, width - 1), random.randint(0, height-1))
        if pos in foods or pos in snake:
            continue
        foods.append(pos)
        break

def move_food(pos):
    i = foods.index(pos)
    del foods[i]
    add_food()

def paint(message):
    surface.fill((0, 0, 0))
    for food in foods:
        pygame.draw.ellipse(surface, (0, 255, 0), Rect(food[0] * 30, food[1] * 30, 30, 30))
    
    for body in snake:
        pygame.draw.rect(surface, (0, 255, 255), Rect(body[0] * 30, body[1] * 30, 30, 30))
    
    for index in range(20):
        pygame.draw.line(surface, (64, 64, 64), (index * 30, 0), (index * 30, 600))
        pygame.draw.line(surface, (64, 64, 64), (0, index * 30), (600, index * 30))

    if message != None:
        surface.blit(message, (150, 300))
    pygame.display.update()

def main():
    myfont = pygame.font.SysFont(None, 80)
    key = K_DOWN
    message = None
    game_over = False
    snake.append((int(width / 2), int(height / 2)))
    fps = 5

    for _ in range(10):
        add_food()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key
        
        if not game_over:
            if key == K_LEFT:
                head = (snake[0][0] - 1, snake[0][1])
            if key == K_RIGHT:
                head = (snake[0][0] + 1, snake[0][1])
            if key == K_UP:
                head = (snake[0][0], snake[0][1] - 1)
            if key == K_DOWN:
                head = (snake[0][0], snake[0][1] + 1)
            
            if head in snake or head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
                message = myfont.render("Game Over!", True, (255, 255, 0))
                game_over = True

            snake.insert(0, head)
            if head in foods:
                move_food(head)
            else:
                snake.pop()

        paint(message)
        fpsclock.tick(fps)

if __name__ == "__main__":
    main()