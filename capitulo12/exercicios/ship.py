import pygame
from settings import Settings


class Ship:
    """A class to manage the rocket."""

    def __init__(self, rocket_game):
        """Initialize the rocket and set its starting position."""
        self.screen = rocket_game.screen
        self.screen_rect = rocket_game.screen.get_rect()
        self.image = pygame.image.load('images/rocketv2.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.settings = Settings()

        # Moviment flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update ship position."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.rocket_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
