#!/usr/bin/python3

import sys
from time import sleep
from random import randint

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from enemies import Enemy


class SidewaysShooter:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Sideways Shooter")

        # Create an instance of game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self._create_enemy()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_enemy()

            self._update_screen()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.background, [0, 0])
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemies.draw(self.screen)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullets position
        self.bullets.update()

        # Get rid of bullets tht have disappeared.
        for bullet in self.bullets.copy():
            # print(bullet)
            if bullet.rect.right >= self.screen_rect.right:
                self.bullets.remove(bullet)
        self._collision()

    def _create_enemy(self):
        """Create one enemy and place in the screen."""
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        enemy.rect.x = self.screen_rect.right
        # print(self.screen_rect.right)
        enemy.rect.y = randint(
            0, self.settings.screen_height - 2 * enemy_height
            )
        # print(enemy.rect.y)
        self.enemies.add(enemy)

    def _update_enemy(self):
        for enemy in self.enemies.copy():
            if enemy.rect.right <= 0:
                self.enemies.remove(enemy)
                self._create_enemy()
        self.enemies.update()
        if not self.enemies:
            self._create_enemy()

        # Look for enemy-ship collosion.
        if pygame.sprite.spritecollideany(self.ship, self.enemies):
            self._ship_hit()

    def _collision(self):
        # Check collitions.
        collitions = pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True
        )
        # Call another enemy if one were destroyed.
        if collitions:
            self._create_enemy()
            self._create_enemy()
        # print(collitions)

    def _ship_hit(self):
        """Respond to the ship being hit by an enemy."""
        if self.stats.ships_left > 0:
            # Decrement ship left.
            self.stats.ships_left -= 1

            # Get rid of any remaining enemies and bullets.
            self.enemies.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_enemy()
            self.ship.center_ship()

            # Pause.
            sleep(1)
        else:
            self.stats.game_active = False


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SidewaysShooter()
    ai.run_game()
