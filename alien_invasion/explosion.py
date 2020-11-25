import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """A class to represent an explosion."""

    def __init__(self, ai_game):
        """Initialize the explosion and set start position."""
        super().__init__()
        explosion_image_list = []
        for num in range(10):
            img_filename = f"images/regularExplosion0{num}.png"
            explosion_image_list.append(img_filename)

# images = []
# for num in range(10):
#     filename = f"images/regularExplosion0{num}.png"
#     images.append(filename)
# print(images)