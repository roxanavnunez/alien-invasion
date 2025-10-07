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
        self.ship_scale = 0.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

         # Alien settings
        self.alien_scale_factor = 0.13
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    
    def resize_image(self, original_size, scale):
        """Resize an image based on a given scale."""
        new_width = int(original_size[0] * scale)
        new_height = int(original_size[1] * scale)
        return (new_width, new_height)

