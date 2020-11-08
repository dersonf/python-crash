import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, sw_game):
        """Initialize the ship and set its starting position."""
        self.screen = sw_game.screen
        self.settings = sw_game.settings
        self.screen_rect = sw_game.screen.get_rect()

        # Load the ship image and get its rect.
        # self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.image.load('images/shipv2.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's horizontal position.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_up and self.rect.up < self.screen_rect.up:
            # self.rect.x += 1
            self.y += self.settings.ship_speed
        if self.moving_down and self.rect.left > 0:
            # self.rect.x -= 1
            self.y -= self.settings.ship_speed

        # Update rect object from self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
