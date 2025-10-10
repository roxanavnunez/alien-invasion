import pygame.font
from pygame.sprite import Group

from ship import Ship
class Scoreboard:
    """A class to report scoring information."""
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.level_rect = None

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Font settings for instructions
        self.inst_font = pygame.font.SysFont(None,30)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_instructions()
    
    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"SCORE: {rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
                       self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"HIGH SCORE: {high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                            self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = f"L: {self.stats.level}"
        self.level_image = self.font.render(level_str, True,
                        self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            new_size = self.settings.resize_image(ship.image.get_size(), self.settings.remain_ship_scale)
            ship.image = pygame.transform.scale(ship.image, new_size)
            ship.rect = ship.image.get_rect()
            ship.rect.x = 10 + ship_number * (ship.rect.width +10)
            ship.rect.y = 10
            self.ships.add(ship)
    
    def prep_instructions(self):
        """Show instructions for the game"""
        instructions1_str = f"P: Pause | ESC: Quit"
        instructions2_str = f"<--   --> Move | SPACE BAR: Shoot"
        self.instructions1_image = self.inst_font.render(instructions1_str, True, self.text_color, self.settings.bg_color)
        self.instructions2_image = self.inst_font.render(instructions2_str, True, self.text_color, self.settings.bg_color)

        # Display instructions1 at the top left of the screen
        ship = Ship(self.ai_game)
        self.instructions1_rect = self.instructions1_image.get_rect()
        self.instructions1_rect.left = self.screen_rect.left + 20
        self.instructions1_rect.top = ship.rect.height - 4

        # Display instructions2 below instructions1
        self.instructions2_rect = self.instructions2_image.get_rect()
        self.instructions2_rect.left = self.screen_rect.left + 20
        self.instructions2_rect.top = self.instructions1_rect.bottom + 10


    def show_score(self):
        """Draw the score, level and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        self.screen.blit(self.instructions1_image,self.instructions1_rect)
        self.screen.blit(self.instructions2_image,self.instructions2_rect)
    
    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()