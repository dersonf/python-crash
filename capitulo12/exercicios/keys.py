import pygame
import sys


class KeysPressed:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the key pressed viewer."""
        pygame.init()

        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Show presses Keys")
        self.bg_color = (200, 200, 200)

    def run_keys(self):
        """Start the main loop."""
        while True:
            self._check_events()
            self._update_screen()
            pygame.display.flip()

    def _update_screen(self):
        """Update images"""
        self.screen.fill(self.bg_color)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    keys = KeysPressed()
    keys.run_keys()
