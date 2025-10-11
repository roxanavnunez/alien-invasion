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
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Load the alien image and set its rect attribute.
        image_path = resource_path('images/alien.png')
        original_image = pygame.image.load(image_path)

        # Scale the alien image to 20% of its original size
        original_size = original_image.get_size()
        new_size = self.settings.resize_image(original_size, self.settings.alien_scale_factor)
        self.image = pygame.transform.scale(original_image, new_size)

        # Get the rect of the scaled image
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        edge = False
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            edge = True
        return edge

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
