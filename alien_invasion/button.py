import pygame.font


class Button:
    def __init__(self, ai_game, msg, position='center'):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the buton.
        self.width, self.height = 200, 50
        self.button_color = (100, 100, 100)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self._buttom_position(position)
        

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color
            )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def _buttom_position(self, position):
        """Choose the button position."""
        if position == 'center':
            self.rect.center = self.screen_rect.center
        elif position == 'left':
            self.rect.center = self.screen_rect.center
            self.rect.x -= 2 * self.width
        elif position == 'right':
            self.rect.center = self.screen_rect.center
            self.rect.x += 2 * self.width




    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
