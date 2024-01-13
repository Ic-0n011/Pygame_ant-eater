import pygame
import sys
import random
ROWS = 10
COLS = 19


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen
        pygame.display.set_caption("Pygame OOP Template")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.screen_width = pygame.display.get_surface().get_size()[0]
        self.screen_height = pygame.display.get_surface().get_size()[1]
        self.cell_size = min(self.screen_width//ROWS, self.screen_height//COLS) + 10
        self.cell_surf = pygame.Surface((self.cell_size, self.cell_size))
        self.cells = [
            [Cell(y=row, x=col, image=self.cell_surf) for col in range(COLS)]
            for row in range(ROWS)
        ]
        self.run()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

    def render_cell(self):
        r = 0
        g = 0
        b = 0
        for row in self.cells:
            for cell in row:
                r += 1
                g += 1
                b += 1
                cell.image.fill((r, g, b))
                self.screen.blit(
                    self.cell_surf,
                    (
                        cell.x * self.cell_size + ((self.screen_height - (self.cell_size * ROWS)) // 2),
                        cell.y * self.cell_size - ((self.screen_height - (self.cell_size * COLS)) // 2)
                     )
                     )

    def update(self):
        # Логика игры
        pass

    def render(self):
        self.screen.fill((255, 255, 255))
        self.render_cell()

        # Render game elements here

        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # Set the frame rate to 60 FPS

        pygame.quit()
        sys.exit()


class Cell():
    """
    класс клетка
    клеток в игре ROWS*COLS
    клетка может обновиться, знает что в ней лежит
    """
    def __init__(self, y, x, image) -> None:
        self.y = y
        self.x = x
        self.content = None
        self.image = image



game = Game()
