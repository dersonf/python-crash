import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star."""

    def __init__(self, star_main):
        """Initialize the star and set the start position"""
        super().__init__()
        self.screen = star_main.screen

        # Load the star image and sets its rect attribute.
        self.image = pygame.image.load('images/starv1.bmp')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store de star's exact horizontal position.
        self.x = float(self.rect.x)
