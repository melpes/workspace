import pygame
import tkinter
############################################################################################
#기본 초기화 (필수)
pygame.init()

#화면 크기 설정
screen_width = 500  # 가로 크기
screen_height= 500 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#프로그램 이름 설정
pygame.display.set_caption("삼색 그림판")

# FPS
clock = pygame.time.Clock()
############################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 캐릭터, 폰트 등)
mouse_position = [0, 0]
mousebutton_state = [0, 0, 0]
running = True
goal_fps = 300
while running:
    dt = clock.tick(goal_fps)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == 1:
                mousebutton_state[0] = 1
            elif pygame.mouse.get_pressed()[0] == 0:
                mousebutton_state[0] = 0
        if mousebutton_state[0] == 1:
            mouse_position = list(pygame.mouse.get_pos())
            print(mouse_position)
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
    
    # 5. 화면에 그리기

    screen.fill((255,255, 255))
    pygame.display.update()

pygame.time.delay(200)

pygame.quit()