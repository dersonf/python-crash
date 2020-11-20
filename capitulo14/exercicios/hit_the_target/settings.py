class Settings:
    """Initialize the static game settings."""

    def __init__(self):
        # Initialize the game settings
        self.bg_color = (0, 0, 0)
        self.screen_width = 1200
        self.screen_height = 800

        # Target settings
        self.target_height = 80
        self.target_width = 8
        self.target_color = (255, 255, 0)
        self.target_direction = 1
        
        # Gun/ship settings
        self.gun_speed = 2.0
        
        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (237, 230, 123)
        self.bullets_allowed = 3
        self.bullet_speed = 4.0
        self.bullets_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughtout the game."""
        self.target_speed = 1.0
        
    def increase_target_speed(self):
        """Increase the target speed"""
        self.target_speed *= self.speedup_scale