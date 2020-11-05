import pygame
import sys
from keys_settings import Settings

class Text:
    """A class to format and show a text."""

    def __init__(self, k_game):
        self.default_text = 'Press any key'
        self.screen = k_game.screen
        self.settings = k_game.settings
        self.screen_rect = k_game.screen.get_rect()
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('Bitstream Charter', 30)
        self.text = self.font.render(self.default_text, True, self.text_color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (
            self.settings.screen_height // 2, self.settings.screen_width // 2
        )

    def update(self, event):
        """Update text info."""
        self.default_text = event

    def blitme(self):
        self.screen.blit(self.text, self.textRect)



class KeysPressed:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the key pressed viewer."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Show presses Keys")
        self.bg_color = (200, 200, 200)
        self.text = Text(self)

    def run_keys(self):
        """Start the main loop."""
        while True:
            self._check_events()
            self._update_screen()
            # self.text.update()
            pygame.display.flip()

    def _update_screen(self):
        """Update images"""
        self.screen.fill(self.bg_color)
        self.text.blitme()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.pressed_key = pygame.key.get_pressed()
                print(self.pressed_key)
                if event.key == pygame.K_q:
                    sys.exit()
                elif self.pressed_key:
                    self.text.update(self.pressed_key)
                    # self.text.default_text = event.key

if __name__ == '__main__':
    keys = KeysPressed()
    keys.run_keys()
