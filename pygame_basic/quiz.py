import pygame
import character_moving_module as cmm
import collision_module as col
import random
############################################################################################
#기본 초기화 (필수)
pygame.init()

#화면 크기 설정
screen_width = 1000  # 가로 크기
screen_height= 700 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#프로그램 이름 설정
pygame.display.set_caption("LAC Game")

# FPS
clock = pygame.time.Clock()
############################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 캐릭터, 폰트 등)
character = pygame.image.load("C:\\Users\\kkang\\Desktop\\과목\\python\\workspace\\pygame_basic\\character.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

enemy = pygame.image.load("C:\\Users\\kkang\\Desktop\\과목\\python\\workspace\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]


enemy_y_pos = 0
enemy_speed = random.uniform(1.0, 2.0)
enemy_x_pos = random.uniform(0.0, screen_width-enemy_width)

to_x = 0
to_y = 0

game_font = pygame.font.Font(None, 40)#폰트 객체 생성 (폰트 , 크기)

running = True
goal_fps = 300

while running:
    dt = clock.tick(goal_fps)
    
    

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        to_x, to_y = cmm.character_moving(event, 0.6)

    character_x_pos += to_x * dt
    enemy_y_pos += enemy_speed * dt
    # 3. 게임 캐릭터 위치 정의
    if (character_x_pos < 0):
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if (character_y_pos < 0):
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 4. 충돌 처리
    character_rect = col.rect_update(character, character_x_pos, character_y_pos)
    
    # 5. 화면에 그리기
    screen.fill((0,120,120))
    screen.blit(character, (character_x_pos, character_y_pos))
    if enemy_y_pos < screen_height:
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()

pygame.time.delay(100)

pygame.quit()