from sys import exit
import pygame
from settings import Settings
from target import Target


class HitTheTarget:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Hit the Target")

        self.target = Target(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.screen.fill(self.settings.bg_color)
            self._check_events()
            self.target.blitme()
            pygame.display.flip()

    def _check_events(self):
        """Check for key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()


if __name__ == '__main__':
    game = HitTheTarget()
    game.run_game()
