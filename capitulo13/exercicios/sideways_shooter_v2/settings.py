import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.background = pygame.image.load('images/background.bmp')
        self.screen_width = 1200
        self.screen_height = 1000
        # self.bg_color = (230, 230, 230)
        # self.bg_color = (0, 0, 255)

        # Ship settings
        self.ship_speed = 2.0

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (237, 230, 123)
        self.bullets_allowed = 4

        # Enemy speed
        self.enemy_min_speed = 2
        self.enemy_max_speed = 6
