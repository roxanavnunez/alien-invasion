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
        self.ship_scale = 0.60

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
    
    def resize_ship_image(self, original_size):
        """Resize the ship image based on the ship scale."""
        new_width = int(original_size[0] * self.ship_scale)
        new_height = int(original_size[1] * self.ship_scale)
        return (new_width, new_height)