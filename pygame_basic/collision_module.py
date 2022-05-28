import pygame

def rect_update(character, character_x_pos, character_y_pos):
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    return character_rect