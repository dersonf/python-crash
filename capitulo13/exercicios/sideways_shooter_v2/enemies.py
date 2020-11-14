from random import randint, choice
import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """A class to represent the enemies."""

    def __init__(self, game_sws):
        """Initilizing the enemies and the positions."""
        super().__init__()
        self.screen = game_sws.screen
        self.settings = game_sws.settings

        # Load the enemy image and sets its rect attribute.
        images = ['images/ufo.bmp', 'images/ufov2.bmp']
        # image = choice(images)
        # print(image)
        self.image = pygame.image.load(choice(images))
        self.rect = self.image.get_rect()

        # Start each new enemy near the top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store de enemy's exact horizontal position.
        self.x = float(self.rect.x)

        # Random speed
        self.speed = randint(
            self.settings.enemy_min_speed, self.settings.enemy_max_speed
            )

    def check_edges(self):
        """Move the alien right or left."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the enemy to the left."""
        # self.x -= self.settings.enemy_speed
        self.rect.x -= self.speed
