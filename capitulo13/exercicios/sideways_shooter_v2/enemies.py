import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """A class to represent the enemies."""

    def __init__(self, game_sws):
        """Initilizing the enemies and the positions."""
        super().__init__()
        self.screen = game_sws.screen
        self.settings = game_sws.settings

        # Load the enemy image and sets its rect attribute.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Start each new enemy near the top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store de enemy's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Move the alien right or left."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
