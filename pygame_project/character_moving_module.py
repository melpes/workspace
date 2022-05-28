import pygame
import math
pygame.init()

to_x = 0
to_y = 0

def leftup():
    return keydown_dict["left"] == 0
def rightup():
    return keydown_dict["right"] == 0
def upup():
    return keydown_dict["up"] == 0
def downup():
    return keydown_dict["down"] == 0
def leftdown():
    return keydown_dict["left"] == 1
def rightdown():
    return keydown_dict["right"] == 1
def updown():
    return keydown_dict["up"] == 1
def downdown():
    return keydown_dict["down"] == 1
keydown_dict = {"left":0, "right":0, "up":0, "down":0}

def character_moving(event, character_speed):
    global to_x
    global to_y
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            keydown_dict["left"] += 1
        if event.key == pygame.K_RIGHT:
            keydown_dict["right"] += 1
        if event.key == pygame.K_UP:
            keydown_dict["up"] += 1
        if event.key == pygame.K_DOWN:
            keydown_dict["down"] += 1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            keydown_dict["left"] -= 1
        if event.key == pygame.K_RIGHT:
            keydown_dict["right"] -= 1
        if event.key == pygame.K_UP:
            keydown_dict["up"] -= 1
        if event.key == pygame.K_DOWN:
            keydown_dict["down"] -= 1
    if (keydown_dict["left"] + keydown_dict["right"]) * (keydown_dict["up"] + keydown_dict["down"]) == 1:
        if keydown_dict["right"] == 0 and keydown_dict["down"] == 0:
            to_x = -character_speed / math.sqrt(2)
            to_y = -character_speed / math.sqrt(2)
        if keydown_dict["right"] == 1 and keydown_dict["down"] == 0:
            to_x = character_speed / math.sqrt(2)
            to_y = -character_speed / math.sqrt(2)
        if keydown_dict["right"] == 0 and keydown_dict["down"] == 1:
            to_x = -character_speed / math.sqrt(2)
            to_y = character_speed / math.sqrt(2)
        if keydown_dict["right"] == 1 and keydown_dict["down"] == 1:
            to_x = character_speed / math.sqrt(2)
            to_y = character_speed / math.sqrt(2)
    else:
        if keydown_dict["left"] + keydown_dict["right"] == 0:
            to_x = 0
        elif keydown_dict["left"] + keydown_dict["right"] == 1:
            if keydown_dict["right"] == 0:
                to_x = -character_speed
            else:
                to_x = character_speed
        elif keydown_dict["left"] + keydown_dict["right"] == 2:
            to_x = 0
        if keydown_dict["up"] + keydown_dict["down"] == 0:
            to_y = 0
        elif keydown_dict["up"] + keydown_dict["down"] == 1:
            if keydown_dict["down"] == 0:
                to_y = -character_speed
            else:
                to_y = character_speed
        elif keydown_dict["up"] + keydown_dict["down"] == 2:
            to_y = 0
    return to_x, to_y

def character_limit(screen_width, screen_height, character_width, character_height, character_x_pos, character_y_pos):
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    return character_x_pos, character_y_pos