from pygame import image


class Gun:
    """A class to manage guns."""

    def __init__(self, htt_game):
        # Initialize the gun and set the position.
        self.screen = htt_game.screen
        self.settings = htt_game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the gun position based on the movement flag."""
        if self.moving_up and self.rect.top > 0:
            # self.rect.x += 1
            self.y -= self.settings.gun_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # self.rect.x -= 1
            self.y += self.settings.gun_speed

        # Update rect object from self.x
        self.rect.y = self.y

    def blitme(self):
        # Draw the lasergun at screen at current position.
        self.screen.blit(self.image, self.rect)
