import pygame
import character_moving_module as cmm
import random
import collision_module as cm
############################################################################################
#기본 초기화 (필수)
pygame.init()

#화면 크기 설정
screen_width = 513  # 가로 크기
screen_height= 700 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#프로그램 이름 설정
pygame.display.set_caption("LAC Game")

# FPS
clock = pygame.time.Clock()
############################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 캐릭터, 폰트 등)

game_font = pygame.font.Font(None, 40)

character =  pygame.image.load("C:\\Users\\kkang\\Desktop\\과목\\python\\workspace\\pygame_basic\\character.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height
character_speed = 0.6

enemy = pygame.image.load("C:\\Users\\kkang\\Desktop\\과목\\python\\workspace\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 1

to_x = 0
to_y = 0,
count = 0

running = True
goal_fps = 300
while running:
    dt = clock.tick(goal_fps)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        to_x, to_y = cmm.character_moving(event, character_speed)
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
    character_rect = cm.rect_update(character, character_x_pos, character_y_pos)
    enemy_rect = cm.rect_update(enemy, enemy_x_pos, enemy_y_pos)
    if character_rect.colliderect(enemy_rect):
        running = False
    # 5. 화면에 그리기

    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width 
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        count += 1

    character_x_pos += to_x * dt
    enemy_y_pos += enemy_speed * dt

    pygame.display.update()
    screen.fill((144, 0, 144))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    score = game_font.render(str(count),True, (0, 0, 0))
    screen.blit(score, (10, 10))

pygame.time.delay(2000)

pygame.quit()