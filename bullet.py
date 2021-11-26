import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create bullet obj at ship location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet rect @ (0,0) and set correct pos
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet pos as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """move bullet up the screen"""
        self.y -= self.settings.bullet_speed
        # Update the rect pos
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
