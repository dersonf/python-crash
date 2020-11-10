import pygame
from sys import exit


class Stars:
    """Initialize the stars class."""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Stars")

    def run_stars(self):
        while True:
            self._check_events()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()


if __name__ == '__main__':
    s = Stars()
    s.run_stars()
