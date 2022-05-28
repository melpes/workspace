import pygame

class MouseControll:
    mouse_position = [0, 0]
    def __init__(self, event):
        pass

    def mousel_down(event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == 1:
                return True
            else:
                return False

    def mousel_up(event):
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pressed()[0] == 0:
                return True
            else:
                return False

    def mousel_motion(event):
        global mouse_position
        if event.type == pygame.MOUSEMOTION:
            # global mouse_position
            mouse_position = list(pygame.mouse.get_pos())
        
        return mouse_position