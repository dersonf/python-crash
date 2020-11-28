import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.background = pygame.image.load('images/background.bmp')
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 45, 180)
        # self.bg_color = (0, 0, 255)

        # FPS value
        self.FPS = 180

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (237, 230, 123)
        self.bullets_allowed_defaut = 3
        self.bullet_speed_default = 3.0

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        # Difficult
        self.difficult = "normal"

        # Default score
        self.default_alien_points = 50

        # Dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Difficult settings.
        if self.difficult == "easy":
            self.bullets_allowed = 3 * self.bullets_allowed_defaut
            self.bullet_speed = 2 * self.bullet_speed_default
            self.alien_points = self.default_alien_points / 2
        elif self.difficult == "normal":
            self.bullets_allowed = self.bullets_allowed_defaut
            self.bullet_speed = 3.0
            self.alien_points = self.default_alien_points
        elif self.difficult == "hard":
            bullets = self.bullets_allowed_defaut / self.bullets_allowed_defaut
            self.bullets_allowed = bullets
            self.bullet_speed = self.bullet_speed_default
            self.alien_points = self.default_alien_points * 2

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
