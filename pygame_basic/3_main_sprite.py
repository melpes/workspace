import pygame
pygame.init()

screen_width = 513
screen_height= 980
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("C:\\Users\\kkang\\Desktop\\과목\\python\\workspace\\pygame_basic\\74932289_p0_master1200.jpg")

character = pygame.image.load("C:\\Users\\kkang\\Desktop\\과목\\python\\workspace\\pygame_basic\\character.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

pygame.display.set_caption("LAC Game")


running = True

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()