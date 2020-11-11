import pygame
from sys import exit
from random import randint
from settings import Settings
from star import Star


class Stars:
    """Initialize the stars class."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption("Stars")
        self.stars = pygame.sprite.Group()
        self._create_constellation()

    def run_stars(self):
        while True:
            self._check_events()
            pygame.display.flip()
            self.stars.draw(self.screen)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()

    def _create_constellation(self):
        """Create the constellation."""
        # Create an star and find the number of stars in a row.
        # Spacing between each star is equal to one star width.
        star = Star(self)
        star_width, star_height = star.rect.size
        number_stars_x = self.settings.screen_width // star_width

        # Determine the number of rows of stars that fit on the screen.
        number_rows = self.settings.screen_height // star_height

        # Create a full constellation.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create a star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + randint(-2, 2) * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + \
            randint(-1, 1) * star.rect.height * row_number
        self.stars.add(star)


if __name__ == '__main__':
    s = Stars()
    s.run_stars()
