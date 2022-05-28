import sys
import random
import pygame
from pygame import *

pygame.init()
pygame.key.set_repeat(5, 5)

background = pygame.display.set_mode((800, 600)) # 화면 크기
fps_clock = pygame.time.Clock()

def main():
    # 변수 목록
    walls = 800 # 벽 개수
    ship_y = 250 # 플레이어 y 좌표
    velocity = 0 # 플레이어 y 속도
    score = 0 # 점수
    slope = random.randint(1, 2) # 동굴의 기울기
    holes = [] # 동굴 구성 직사각형 저장용 리스트
    gameover = False # 게임 오버 여부 판정
    rocket = pygame.image.load("pygame_project/rocket.jpeg")
    bang = pygame.image.load("pygame_project/bang.jpg")
    fps = 120
    sysfont = pygame.font.SysFont(None, 36)
    number = pygame.font.SysFont(None, 100)
    wall_width = 1
    ship_grabity = 0.15
    starting_count = 0

    for xpos in range(walls):
        holes.append(Rect(xpos * wall_width, 100, wall_width, 400))
    
    while True:
        # 이벤트 처리
        is_space_down = False
        fps_clock.tick(fps)
        starting_count += 1
        print(starting_count)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True

        if starting_count < 60:
            counting = number.render("3", True, (255, 255, 255))
        elif starting_count < 120:
            counting = number.render("2", True, (255, 255, 255))
        elif starting_count < 180:
            counting = number.render("1", True, (255, 255, 255))
        elif not gameover:
            if slope == 0:
                slope = 0.001

            # 이동
            score += 10
            velocity += -ship_grabity if is_space_down else ship_grabity
            ship_y += velocity
        
            # 화면 이동
            edge = holes[-1].copy()
            test = edge.move(0, slope)
            if test.top <= 0 or test.bottom >= 600:
                slope = random.randint(1, 2) * (-1 if slope > 0 else 1)
                edge.inflate_ip(0, -20)
            edge.move_ip(wall_width, slope)
            holes.append(edge)
            del holes[0]
            holes = [x.move(-wall_width, 0) for x in holes]

            if holes[0].top > ship_y or holes[0].bottom < ship_y + 80:
                gameover = True
        
        # 그리기
        background.fill((0, 200, 0))
        for hole in holes:
            pygame.draw.rect(background, (0, 0, 0), hole)
        background.blit(rocket, (0, ship_y))
        score_image = sysfont.render(f"score is {score}", True, (0, 0, 225))
        background.blit(score_image, (600, 20))

        if gameover:
            background.blit(bang, (0, ship_y - 40))
        if starting_count < 180:
            background.blit(counting, (400, 300))

        pygame.display.update()

if __name__ == "__main__":
    main()