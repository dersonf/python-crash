import logging

import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """A class to represent an explosion."""

    def __init__(self, ai_game, position):
        """Initialize the explosion and set start position."""
        super().__init__()
        # explosions_image_list = []
        # for num in range(9):
        #     img_filename = f"images/regularExplosion0{num}.png"
        #     logging.debug(f"{img_filename}")
        #     image = pygame.image.load(img_filename).convert()
        #     image_sized = pygame.transform.scale(image, (60, 60))
        #     explosions_image_list.append(image_sized)
        # logging.debug(f"{explosions_image_list}")
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        image = pygame.image.load('images/regularExplosion00.png').convert()
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = position
        # self.frame = 0
        # self.last_update = pygame.time.get_ticks()
        # self.frame_rate = 50
        

    # def update(self):
    #     now = pygame.time.get_ticks()
    #     if now - self.last_update > self.frame_rate:
    #         self.last_update = now
    #         self.frame += 1
    #         if self.frame == len(explosions_image_list):
    #             self.kill()
    #         else:
    #             position = self.rect.center
    #             self.image = explosions_image_list[self.frame]
    #             self.rect = self.image.get_rect()
    #             self.rect.center = position
    #             self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)