import json
class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_paused = False

        # Load the high score from a file.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def save_high_score(self):
        """Save the high score to a file."""
        filename = 'high_score.json'
        with open(filename, 'w') as f:
            json.dump(self.high_score, f)
    
    def load_high_score(self):
        """Load the high score from a file."""
        filename = 'high_score.json'
        try:
            with open(filename) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            return 0
        else:
            return self.high_score
