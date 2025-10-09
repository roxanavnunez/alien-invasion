import pygame
from bullet import Bullet

class AlienBullet(Bullet):
    """A class to manage bullets fired from aliens."""
    
    def __init__(self, ai_game, alien):
        """Create a bullet object at the alien's current position."""
        super().__init__(ai_game)
        self.rect.midbottom = alien.rect.midtop
        self.y = float(self.rect.y)
        self.color = (255, 0, 0)
    
    def update(self):
        """Move the bullet down the screen."""
        # Update the decimal position of the bullet.
        self.y += self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y