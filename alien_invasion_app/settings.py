class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.fullscreen = False

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Alien settings
        self.scale_factor = 0.2
    
    def resize_alien_image(self, original_size):
        """Resize the alien image based on the scale factor."""
        new_width = int(original_size[0] * self.scale_factor)
        new_height = int(original_size[1] * self.scale_factor)
        return (new_width, new_height)