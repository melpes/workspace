import sys
from math import radians, sin, cos
from random import randint
import pygame
from pygame.constants import KSCAN_INTERNATIONAL1, K_a, K_d, K_s, K_w
from pygame.draw import rect
from pygame.locals import Rect, QUIT, KEYDOWN, KEYUP, K_SPACE, K_LEFT, K_RIGHT, K_UP, K_DOWN,\
    K_w, K_a, K_s, K_d

pygame.init()
pygame.key.set_repeat(5, 5)
surface = pygame.display.set_mode((800, 800))
fpsclock = pygame.time.Clock()
fps = 20

class Drawable:
    def __init__(self, rect):
        self.rect = rect
        self.step = [0, 0]

    def move(self):
        rect = self.rect.center
        xpos = (rect[0] + self.step[0]) % 800
        ypos = (rect[1] + self.step[1]) % 800
        self.rect.center = (xpos, ypos)

class Rock(Drawable):
    def __init__(self, pos, size):
        super(Rock, self).__init__(Rect(0, 0, size, size))
        self.rect.center = pos
        self.image = pygame.image.load("pygame_project/games/asteroid/rock.png")
        self.theta = randint(0, 360)
        self.size = size
        self.power = 128 / size
        self.step[0] = cos(radians(self.theta)) * self.power
        self.step[1] = sin(radians(self.theta)) * -self.power

    def draw(self):
        rotated = pygame.transform.rotozoom(self.image, self.theta, self.size / 64)
        rect = rotated.get_rect()
        rect.center = self.rect.center
        surface.blit(rotated, rect)

    def tick(self):
        self.theta += 3
        self.move()

class Shot(Drawable):
    def __init__(self):
        super().__init__(Rect(0, 0, 6, 6))
        self.count = 20
        self.power = 40
        self.max_count = 20

    def draw(self):
        if self.count < self.max_count:
            pygame.draw.rect(surface, (225, 225, 0), self.rect)

    def tick(self):
        self.count += 1
        self.move()

class Ship(Drawable):
    def __init__(self):
        super().__init__(Rect(355, 370, 90, 60))
        self.theta = 0
        self.power = 0
        self.accel = 0
        self.explode = False
        self.image = pygame.image.load("pygame_project/games/asteroid/ship.png")
        self.bang = pygame.image.load("pygame_project/games/asteroid/bang.png")

    def draw(self):
        rotated = pygame.transform.rotate(self.image, self.theta)
        rect = rotated.get_rect()
        bang_rect = self.image.get_rect()
        bang_rect.center = self.rect.center
        rect.center = self.rect.center
        if self.explode:
            surface.blit(self.bang, bang_rect)
        else:
            surface.blit(rotated, rect)
        
    def tick(self):
        self.power += self.accel
        self.power *= 0.94
        self.accel *= 0.94
        self.step[0] = cos(radians(self.theta)) * self.power
        self.step[1] = sin(radians(self.theta)) * -self.power
        self.move()

def key_event_handler(keymap, ship):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if not event.key in keymap:
                keymap.append(event.key)
        elif event.type == KEYUP:
            keymap.remove(event.key)

    if K_LEFT in keymap:
        ship.theta += 5
    if K_RIGHT in keymap:
        ship.theta -= 5
    if K_UP in keymap:
        ship.accel = min(3, ship.accel + 0.2)
    if K_DOWN in keymap:
        ship.accel = max(-1.5, ship.accel - 0.1)

    if K_a in keymap:
        ship.theta += 5
    if K_d in keymap:
        ship.theta -= 5
    if K_w in keymap:
        ship.accel = min(3, ship.accel + 0.2)
    if K_s in keymap:
        ship.accel = max(-1.5, ship.accel - 0.1)

def main():
    sysfont = pygame.font.SysFont(None, 72)
    scorefont = pygame.font.SysFont(None, 36)
    message_clear = sysfont.render("!!CLEARED!!", True, (0, 255, 225))
    message_over = sysfont.render("GAME OVER!!", True, (0, 255, 225))
    message_rect = message_clear.get_rect()
    message_rect.center = (400, 400)

    keymap = []
    shots = []
    rocks = []
    ship = Ship()
    game_over = False
    score = 0
    back_x, back_y = (0, 0)
    back_image = pygame.image.load("pygame_project/games/asteroid/bg.png")
    back_image = pygame.transform.scale2x(back_image)

    while len(shots) < 7:
        shots.append(Shot())

    while len(rocks) < 7:
        pos = (randint(0, 800), randint(0, 800))
        rock = Rock(pos, 64)
        if not rock.rect.colliderect(ship.rect):
            rocks.append(rock)
    
    while True:
        key_event_handler(keymap, ship)

        if not game_over:
            ship.tick()
            print(keymap)

            for rock in rocks:
                rock.tick()
                if rock.rect.colliderect(ship.rect):
                    ship.explode = True
                    game_over = True
                
            fire = False
            for shot in shots:
                if shot.count < shot.max_count:
                    shot.tick()

                    hit = None
                    for rock in rocks:
                        if rock.rect.colliderect(shot.rect):
                            hit = rock
                        
                    if hit != None:
                        score += hit.rect.width * 10
                        shot.count = shot.max_count
                        rocks.remove(hit)
                        if hit.rect.width > 16:
                            rocks.append(Rock(hit.rect.center, hit.rect.width / 2))
                            rocks.append(Rock(hit.rect.center, hit.rect.width / 2))
                        if len(rocks) == 0:
                            game_over = True

                elif not fire and K_SPACE in keymap:
                    shot.count = 0
                    shot.rect.center = ship.rect.center
                    shot_x = shot.power * cos(radians(ship.theta))
                    shot_y = shot.power * -sin(radians(ship.theta))
                    shot.step = (shot_x, shot_y)
                    fire = True

        back_x = (back_x + ship.step[0] / 2) % 1600
        back_y = (back_y + ship.step[1] / 2) % 1600
        surface.fill((0, 0, 0))
        surface.blit(back_image, (-back_x, -back_y), (0, 0, 3200, 3200))

        ship.draw()

        for shot in shots:
            shot.draw()
        for rock in rocks:
            rock.draw()

        score_str = str(score).zfill(6)
        score_image = scorefont.render(score_str, True, (0, 255, 0))
        surface.blit(score_image, (700, 10))

        if game_over:
            if len(rocks) == 0:
                surface.blit(message_clear, message_rect.topleft)
            else:
                surface.blit(message_over, message_rect.topleft)

        pygame.display.update()
        fpsclock.tick(fps)

if __name__ == "__main__":
    main()