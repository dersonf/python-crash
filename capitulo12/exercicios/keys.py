import pygame
import sys
from keys_settings import Settings
from text import Text

class KeysPressed:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the key pressed viewer."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Show pressed Key")
        self.bg_color = (200, 200, 200)

        self.text = Text(self)

    def run_keys(self):
        """Start the main loop."""
        while True:
            self._check_events()
            self._update_screen()
            pygame.display.flip()

    def _update_screen(self):
        """Update images"""
        self.text.blitme()
        self.screen.fill(self.bg_color)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()


if __name__ == '__main__':
    keys = KeysPressed()
    keys.run_keys()
