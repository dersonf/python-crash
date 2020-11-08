import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.background = pygame.image.load('images/background.bmp')
        self.screen_width = 1000
        self.screen_height = 600
        # self.bg_color = (230, 230, 230)
        # self.bg_color = (0, 0, 255)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (237, 230, 123)
        self.bullets_allowed = 3