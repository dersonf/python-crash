class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, htt_game):
        """Initialize statistics."""
        self.settings = htt_game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.bullets_left = self.settings.bullet_limit
