class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230, 230, 230)
        self.fullscreen = False

        # Ship settings
        self.ship_limit = 3
        self.ship_scale = 0.45
        self.remain_ship_scale = 0.75

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

         # Alien settings
        self.alien_scale_factor = 0.13
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def resize_image(self, original_size, scale):
        """Resize an image based on a given scale."""
        new_width = int(original_size[0] * scale)
        new_height = int(original_size[1] * scale)
        return (new_width, new_height)
    
    def initialize_dynamic_settings(self): 
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2.5
        self.bullet_speed = 4.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Scoring settings
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
