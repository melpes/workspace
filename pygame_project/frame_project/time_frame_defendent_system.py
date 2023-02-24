import pygame
import time
############################################################################################
#기본 초기화 (필수)
pygame.init()

def main() -> None:
    scr = Screen((1000, 600), "L", 1)
    while True:
        running = scr.time_handling()
        if running == False:
            break
        if scr.now - scr.last_update_time >= scr.fps:
            scr.update()
    scr.end()


class Screen:
    def __init__(self, size : tuple, name : str, fps) -> None:
        self.screen_size : tuple = size
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.last_update_time = time.time()

    def event_handling(self) -> bool:
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        return running

    def time_handling(self):
        dt = self.clock.tick(30)
        self.now = time.time()
        print("time updating")
        running = self.event_handling()
        return running

    def update(self):
        self.last_update_time = time.time()
        pygame.display.update()
        print("screen updating")
    
    def end(self):
        pygame.time.delay(200)
        pygame.quit()

if __name__ == "__main__":
    main()