import logging

import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """A class to represent an explosion."""

    def __init__(self):
        """Initialize the explosion and set start position."""
        super().__init__()
        self.explosions_image_list = []
        for num in range(9):
            img_filename = f"images/regularExplosion0{num}.png"
            image = pygame.image.load(img_filename).convert()
            image.set_colorkey((0, 0, 0))
            image_sized = pygame.transform.scale(image, (55, 55))
            self.explosions_image_list.append(image_sized)
        logging.debug(f"{self.explosions_image_list[0]}")
        # image = pygame.image.load('images/regularExplosion00.png').convert()
        # image.set_colorkey((0, 0, 0))
        # self.image = pygame.transform.scale(image, (50, 50))
        # self.last_update = pygame.time.get_ticks()
        # self.frame_rate = 50

    def update(self, ai_game, position):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        if self.frame >= len(self.explosions_image_list):
            self.frame = 0
        self.image = self.explosions_image_list[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.frame += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)