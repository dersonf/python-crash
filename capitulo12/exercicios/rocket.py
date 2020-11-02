#!/usr/bin/python3

import pygame
import sys
from ship import Ship


class Rocket:
    """A class to manage resources and behavior."""

    def __init__(self):
        """Initialize a game and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.backgroud = pygame.image.load('images/backgroud.bmp')
        pygame.display.set_caption("Rocket")

        self.rocket = Ship(self)

    def run_game(self):
        while True:
            self.check_events()
            pygame.display.flip()
            self.screen.blit(self.backgroud, [0, 0])
            self.rocket.blitme()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    rocket = Rocket()
    rocket.run_game()