import pygame
from pygame.sprite import Sprite


class RainDrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, rain_main):
        """Initialize the raindrop and set the start position"""
        super().__init__()
        self.screen = rain_main.screen
        self.settings = rain_main.settings
        self.screen_rect = rain_main.screen.get_rect()

        # Load the raindrop image and sets its rect attribute.
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store de raindrop's exact vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop to the bottom."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
        if self.rect.top >= self.screen_rect.bottom:
            self.y = self.screen_rect.top - 60
