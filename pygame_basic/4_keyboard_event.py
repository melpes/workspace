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

to_x = 0
to_y = 0

running = True

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    if (character_x_pos < 0):
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if (character_y_pos < 0):
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    character_x_pos += to_x
    character_y_pos += to_y

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()