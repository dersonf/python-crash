from pygame import Surface


class Target:
    """A class to represent a target."""

    def __init__(self, htt_game):
        """Initialize the mark."""
        self.screen = htt_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = htt_game.settings

        # Initialize the target
        self.image = Surface([self.settings.target_width,
                              self.settings.target_height])
        self.image.fill(self.settings.target_color)

        # Fetch the target
        self.rect = self.image.get_rect()

        # Call the start position
        self.start_position()

    def start_position(self):
        # Start target at right side and middle of screen.
        self.rect.x = self.screen_rect.right - \
            2 * self.settings.target_width
        self.rect.y = self.screen_rect.centery - \
            self.settings.target_height / 2

        # Store the exact target position
        self.y = float(self.rect.y)

    def update(self):
        """Move the target up and down."""
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = self.y

    def blitme(self):
        """Draw the target."""
        self.screen.blit(self.image, self.rect)
