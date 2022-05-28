import pygame
pygame.init()

screen_width = 513
screen_height= 980
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("C:\\Users\\kkang\\Desktop\\과목\\python\\workspace\\pygame_basic\\74932289_p0_master1200.jpg")
pygame.display.set_caption("LAC Game")


running = True

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False


    screen.blit(background, (0, 0))

    pygame.display.update()

pygame.quit()