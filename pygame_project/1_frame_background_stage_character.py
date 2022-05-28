import pygame
import os
import character_moving_module as cmm
############################################################################################
#기본 초기화 (필수)
pygame.init()

#화면 크기 설정
screen_width = 640  # 가로 크기
screen_height= 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#프로그램 이름 설정
pygame.display.set_caption("LAC Ball")

# FPS
clock = pygame.time.Clock()
############################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 캐릭터, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")

# 배경 이미지
background = pygame.image.load(os.path.join(image_path, "background.jpg"))

# 스테이지
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height - stage_height

character_to_x = 0
character_to_y = 0
character_speed = 1

# 무기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]

weapons = []
weapon_speed = 2

running = True
goal_fps = 300
while running:
    dt = clock.tick(goal_fps)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        character_to_x, character_to_y = cmm.character_moving(event, character_speed)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + character_width / 2 - weapon_width / 2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
    # 3. 게임 캐릭터 위치 정의
    character_x_pos, character_y_pos = cmm.character_limit(screen_width, screen_height, character_width, character_height, character_x_pos, character_y_pos)
    character_x_pos += character_to_x * dt

    weapons = [ [w[0], w[1] - weapon_speed * dt] for w in weapons]
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > -weapon_height ]

    
    # 4. 충돌 처리
    
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update()

pygame.time.delay(200)

pygame.quit()