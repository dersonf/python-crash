import pygame


class Ship:
    """A class to manage the rocket."""

    def __init__(self, rocket_game):
        """Initialize the rocket and set its starting position."""
        self.screen = rocket_game.screen
        self.screen_rect = rocket_game.screen.get_rect()
        self.image = pygame.image.load('images/rocketv2.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        # Moviment flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update ship position."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
