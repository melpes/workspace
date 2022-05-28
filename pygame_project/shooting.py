import pygame
import BasicHPmanagement as BHm
import average_fps_module as afm
############################################################################################
#기본 초기화 (필수)
pygame.init()

#화면 크기 설정
screen_width = 500  # 가로 크기
screen_height= 400 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#프로그램 이름 설정
pygame.display.set_caption("LAC Game")

# FPS
clock = pygame.time.Clock()
############################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 캐릭터, 폰트 등)
character = BHm.CharacterBase(100, 50, 0, 20, 4)

game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트 , 크기)
kkey = 0
dmm = 0
goal_fps = 300
efps = goal_fps
n = 0

running = True

while running:
    dt = clock.tick(goal_fps)
    efps, n = afm.average_fps(efps, n, clock.get_fps())
    print(clock.get_fps(), efps)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dmm = character.get_damaged(20)
            if event.key == pygame.K_DOWN:
                kkey = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                kkey = 0
    if kkey == 1:
        character.increasing_fatigue(0.1)
    # 3. 게임 캐릭터 위치 정의
    # print(character.hemorrhage_counting / 1000 * efps, "\t", efps)
    # 4. 충돌 처리
    if (character.hemorrhage_counting < character.hemorrhage_time * 1000 / efps) and (dmm != 0):
        character.hemorrhage(dmm , efps)
    # 5. 화면에 그리기 
    health = game_font.render(str(int(character.currenthealth * 10) / 10)+"/"+str(character.maxhealth), True, (255,255,255))
    shield = game_font.render(str(character.shield), True, (255,255,255))
    fatigue = game_font.render(str(character.fatigue), True, (255,255,255))
    accdamage = game_font.render(str(character.accumulated_damage), True, (255,255,255))

    screen.fill((0, 0, 0))
    screen.blit(health, (10, 10))
    screen.blit(shield, (10, 70))
    screen.blit(fatigue, (10, 130))
    screen.blit(accdamage, (10, 190))

    pygame.display.update()
pygame.time.delay(200)

pygame.quit()