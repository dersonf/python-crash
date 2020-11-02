#!/usr/bin/python3

import pygame
import sys


class Rocket:
    """A class to manage resources and behavior."""

    def __init__(self):
        """Initialize a game and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket")

    def run_game(self):
        while True:
            pygame.display.flip()
            self.check_events()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    rocket = Rocket()
    rocket.run_game()