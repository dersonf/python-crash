from sys import exit
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from target import Target
from gun import Gun
from bullet import Bullet


class HitTheTarget:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Hit the Target")
        # self.screen_rect = self.screen.get_rect()

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.target = Target(self)
        self.gun = Gun(self)
        self.bullets = pygame.sprite.Group()

        # Make the Play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self._target_direction()
                self.gun.update()
                self.target.update()
                self._update_bullets()

            self._screen_update()

    def _check_events(self):
        """Check for key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _check_keydown_events(self, event):
        """Respond for keypresses."""
        if event.key == pygame.K_q:
            exit()
        elif event.key == pygame.K_UP:
            self.gun.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.gun.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond for key releases."""
        if event.key == pygame.K_UP:
            self.gun.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.gun.moving_down = False

    def _start_game(self):
        """Start a new game."""
        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True

        # Get rid of any remaining aliens and bullets.
        self.target.start_position()
        self.bullets.empty()

        self.gun.start_position()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _target_direction(self):
        """Change target direction if hit the edges."""
        if self.target.rect.bottom >= self.settings.screen_height \
                or self.target.rect.top <= 0:
            self.settings.target_direction *= -1

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        if self.stats.bullets_left > 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.stats.bullets_left -= 1

    def _screen_update(self):
        self.screen.fill(self.settings.bg_color)
        self.target.blitme()
        self.gun.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullets position
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.settings.screen_width:
                self.bullets.remove(bullet)
        self._check_bullet_target_collisions()

    def _check_bullet_target_collisions(self):
        """Respond to bullet-target collisions."""
        # Remove any bullets and aliens that have collided.
        if pygame.sprite.spritecollideany(self.target, self.bullets):
            self.bullets.empty()
            self.stats.bullets_left = 3
            self.target.start_position()
        if not self.bullets and self.stats.bullets_left == 0:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


if __name__ == '__main__':
    game = HitTheTarget()
    game.run_game()
