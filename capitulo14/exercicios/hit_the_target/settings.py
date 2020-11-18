class Settings:
    """Initialize the settings."""

    def __init__(self):
        # Initialize the game settings.
        self.bg_color = (0, 0, 0)
        self.screen_width = 1200
        self.screen_height = 800

        # Target settings.
        self.target_height = 80
        self.target_width = 8
        self.target_color = (255, 255, 0)
        self.target_speed = 1
        self.target_direction = 1

        # Gun settings
        self.gun_speed = 2

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (237, 230, 123)
        self.bullets_allowed = 3
