import pygame


class Ship:
    """A class to manage the rocket."""

    def __init__(self, rocket_game):
        """Initialize the rocket and set its starting position."""
        self.screen = rocket_game.screen
        self.screen_rect = rocket_game.screen.get_rect()
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
