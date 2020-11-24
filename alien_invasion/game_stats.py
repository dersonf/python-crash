class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        # High score should never be reset.
        self.high_score = 0
        self.handle_high_score("r")

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def handle_high_score(self, action):
        """Read the high score stored in file."""
        filename = 'highscore'
        try:
            with open(filename, 'r+') as f:
                if action == "r":
                    self.high_score = int(f.read().strip())
                if action == "w":
                    hs = str(self.high_score)
                    f.write(hs)
        except FileNotFoundError:
            with open(filename, 'w') as f:
                f.write("0")
