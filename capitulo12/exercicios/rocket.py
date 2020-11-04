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
            self.rocket.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond for keypresses."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond for key release."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False


if __name__ == '__main__':
    rocket = Rocket()
    rocket.run_game()
