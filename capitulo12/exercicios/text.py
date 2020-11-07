import pygame

class Text:
    """Class with a text settings."""

    def __init__(self, k_pressed):
        """Initializing class."""
        self.screen = k_pressed.screen
        self.screen_rect = k_pressed.screen.get_rect()
        self.msg = "Press any key."
        self.msg_color = (0, 0, 0)
        self.msg_bg_color = (200, 200, 200)
        self.f = pygame.font.SysFont(None, 48)
        
        self.msg_image = self.f.render(self.msg, True, self.msg_color, self.msg_bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)
