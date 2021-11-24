import pygame

class Ship:
    """Class to manage the ship"""

    def __init__(self,ai_game):
        """init the ship and set its start pos"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and get it's rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for ships horitontal position
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ship'd position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # update rect obj from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
