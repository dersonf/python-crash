#!/usr/bin/python3

import sys
from time import sleep
import logging

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.fpsClock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to score game statistics,
        # and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self._create_fleet()

        # Make the buttons.
        self.play_button = Button(self, "Play")
        self.easy_button = Button(self, "easy", "easy")
        self.normal_button = Button(self, "normal", "normal")
        self.hard_button = Button(self, "hard", "hard")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.handle_high_score('w')
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_button(mouse_pos)

    def _check_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos) \
                and not self.stats.game_active:
            self._start_game()
        if self.easy_button.rect.collidepoint(mouse_pos) \
                and not self.stats.game_active:
            self.settings.difficult = "easy"
        if self.normal_button.rect.collidepoint(mouse_pos) \
                and not self.stats.game_active:
            self.settings.difficult = "normal"
        if self.hard_button.rect.collidepoint(mouse_pos) \
                and not self.stats.game_active:
            self.settings.difficult = "hard"

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT or \
                event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or \
                event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.stats.handle_high_score('w')
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.stats.game_active:
            logging.debug('p key to start pressed')
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT or \
                event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or \
                event.key == pygame.K_a:
            self.ship.moving_left = False

    def _start_game(self):
        """Start a new game."""
        # Reset the game settings.
        logging.debug('Start game')
        self.settings.initialize_dynamic_settings()

        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Get rid of any remaining aliens and bullets.
        logging.debug('Empty aliens')
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship.
        logging.debug('Creating fleet.')
        self._create_fleet()
        logging.debug(f"{len(self.aliens)} aliens.")
        self.ship.center_ship()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

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
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Make the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.normal_button.draw_button()
            self.hard_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        self.fpsClock.tick(self.settings.FPS)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullets position
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Calling the method to check collision.
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        logging.debug(f"{len(self.aliens)}")
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            logging.debug('Hit an alien')
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self._start_new_level()

    def _start_new_level(self):
        """Destroy existing bullets, create new fleet and raise difficult."""
        logging.debug("Level up.")
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        logging.debug('Exec method to create fleet.')
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the scren.
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
            )
        number_rows = available_space_y // (2 * alien_height)

        # Create a full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
        logging.debug('Fleet created.')

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
         then update the position of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of remaining aliens an bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any alien have reached the botttom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break


if __name__ == '__main__':
    # Debug mode to find error, switch INFO by DEBUG.
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
        )
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
