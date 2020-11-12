import pygame
from sys import exit
from settings import Settings
from raindrop import RainDrop


class Rain:
    """Initialize the rain class."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.bg_color = self.settings.bg_color
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption("Rain")
        self.raindrops = pygame.sprite.Group()
        self._create_rain()

    def run_rain(self):
        while True:
            self._check_events()
            self.screen.fill(self.bg_color)
            self.raindrops.draw(self.screen)
            self.raindrops.update()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()

    def _create_rain(self):
        """Create a rain."""
        # Create a raindrop and find the number of raindrops in a row.
        # Spacing between each raindrop is equal to one raindrop width.
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        number_raindrops_x = self.settings.screen_width // (2 * raindrop_width)

        # Determine the number of rows of raindrops that fit on the screen.
        number_rows = self.settings.screen_height // (2 * raindrop_height) + 1

        # Create a full rain.
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Create a raindrop and place it in the row."""
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.y = raindrop_height + 2 * raindrop_height * row_number
        raindrop.rect.y = raindrop.y
        raindrop.rect.x = raindrop.rect.width + \
            2 * raindrop.rect.width * raindrop_number
        self.raindrops.add(raindrop)


if __name__ == '__main__':
    s = Rain()
    s.run_rain()
