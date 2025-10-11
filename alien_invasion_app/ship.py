import pygame
import sys
import os
from pygame.sprite import Sprite    

def resource_path(relative_path):
    """Get abosolute path"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)
class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and resize it
        image_path = resource_path('images/ship.png')
        original_image = pygame.image.load(image_path).convert_alpha()
        original_size = original_image.get_size()
        new_size = self.settings.resize_image(original_size, self.settings.ship_scale)
        self.image = pygame.transform.scale(original_image, new_size)

        # Get the rect of the image.
        self.rect = self.image.get_rect()

        # Initial position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        # Store a float value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; starting with no movement.
        self.moving_right = False
        self.moving_left = False
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.bottom = self.screen_rect.bottom - 10
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
