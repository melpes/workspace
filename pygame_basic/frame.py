import pygame

def main() -> None:
    game = Game(size=(400, 200), title="practice", fps=30)
    while game.is_running:
        dt = game.get_dt()
        game.handle_event()
        game.blit_display()

    game.exit()

class Game:
    def __init__(self, size, title, fps) -> None:
        pygame.init()
        self.screen_size = size
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("practice")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = fps

    def get_dt(self) -> float:
        print("type check : float ==", type(self.clock.tick(self.fps)))
        return self.clock.tick(self.fps)

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def blit_display(self) -> None:
        pygame.display.update()

    def exit(self) -> None:
        pygame.time.delay(200)
        pygame.quit()

if __name__ == "__main__":
    main()
