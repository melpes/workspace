import pygame
############################################################################################
#기본 초기화 (필수)
pygame.init()

#화면 크기 설정
screen_width = 513  # 가로 크기
screen_height= 980 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#프로그램 이름 설정
pygame.display.set_caption("LAC Game")

# FPS
clock = pygame.time.Clock()
############################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 캐릭터, 폰트 등)

running = True
goal_fps = 30
while running:
    dt = clock.tick(goal_fps)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
    
    # 5. 화면에 그리기

    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()
