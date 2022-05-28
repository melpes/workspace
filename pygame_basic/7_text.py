import pygame
import average_fps_module as afm
import character_moving_module as cmm
import collision_module as col
import random
pygame.init()

#스크린 및 배경
screen_width = 513
screen_height= 980
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("C:\\Users\\kkang\\Desktop\\과목\\python\\workspace\\pygame_basic\\74932289_p0_master1200.jpg")

#캐릭터 세부사항
character = pygame.image.load("C:\\Users\\kkang\\Desktop\\과목\\python\\workspace\\pygame_basic\\character.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

#프로그램 이름 설정
pygame.display.set_caption("LAC Game")

clock = pygame.time.Clock()

to_x = 0
to_y = 0

running = True
goal_fps = 300

enemy = pygame.image.load("C:\\Users\\kkang\\Desktop\\과목\\python\\workspace\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

enemy_x_pos1 = screen_width / 2 - enemy_width / 2
enemy_y_pos1 = (screen_height / 2) - enemy_height / 2
enemy_x_pos2 = screen_width / 2 - enemy_width / 2
enemy_y_pos2 = (screen_height / 2) - enemy_height / 2

# 폰트 정의
game_font = pygame.font.Font(None, 40)#폰트 객체 생성 (폰트 , 크기)

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()


while running:
    dt = clock.tick(goal_fps)
    # print(afm.average_fps(goal_fps))#프로그램 가동 이후부터 현재까지의 평균 fps 출력


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        to_x, to_y = cmm.character_moving(event, 0.6)#감지되는 이벤트와 속도를 넣으면 방향키로 플레이어 이동
    
            
    if (character_x_pos < 0):
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if (character_y_pos < 0):
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    if (enemy_x_pos1 < 0):
        enemy_x_pos1 = 0
    elif enemy_x_pos1 > screen_width - enemy_width:
        enemy_x_pos1 = screen_width - enemy_width
    if (enemy_y_pos1 < 0):
        enemy_y_pos1 = 0
    elif enemy_y_pos1 > screen_height - enemy_height:
        enemy_y_pos1 = screen_height - enemy_height
    if (enemy_x_pos2 < 0):
        enemy_x_pos2 = 0
    elif enemy_x_pos2 > screen_width - enemy_width:
        enemy_x_pos2 = screen_width - enemy_width
    if (enemy_y_pos2 < 0):
        enemy_y_pos2 = 0
    elif enemy_y_pos2 > screen_height - enemy_height:
        enemy_y_pos2 = screen_height - enemy_height

    character_rect = col.rect_update(character, character_x_pos, character_y_pos)
    enemy_rect1 = col.rect_update(enemy, enemy_x_pos1, enemy_y_pos1)
    enemy_rect2 = col.rect_update(enemy, enemy_x_pos2, enemy_y_pos2)
    if character_rect.colliderect(enemy_rect1) or character_rect.colliderect(enemy_rect2):
        print("충돌 !!")
        running = False

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    enemy_x_pos1 += random.random() * random.randrange(-1, 2, 2) * dt * 2
    enemy_y_pos1 += random.random() * random.randrange(-1, 2, 2) * dt * 2
    enemy_x_pos2 += random.random() * random.randrange(-1, 2, 2) * dt * 2
    enemy_y_pos2 += random.random() * random.randrange(-1, 2, 2) * dt * 2

    screen.blit(background, (0, 0))
    # screen.fill((0,0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos1, enemy_y_pos1))
    screen.blit(enemy, (enemy_x_pos2, enemy_y_pos2))

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000#경과 시간을 1000으로 나누어 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # 출력할 글자, 안티앨리어스?, 글자 색상 튜플로 RGB
    screen.blit(timer, (10, 10))
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False
    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()