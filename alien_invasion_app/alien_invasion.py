import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics and scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Create a ship, a group of bullets, and a group of aliens.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Start in an inactive state.
        self.game_active = False

        # Make the Play button.
        self.play_button = Button(self, "Play")
       
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active and not self.stats.game_paused:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()         
            self.clock.tick(60)
    
    def _close_game(self):
        """Close the game and save high score."""
        self.stats.save_high_score()
        sys.exit()
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._close_game()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            self._close_game()
        elif event.key == pygame.K_f:
            self._toggle_fullscreen()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key ==pygame.K_p:
            if self.game_active:
                self.stats.game_paused = not self.stats.game_paused

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _play_game(self):
        """Start a new game."""
        if not self.game_active:
            # Reset the game statistics and settings.
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True
            self.settings.initialize_dynamic_settings()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._play_game()
        
    def _toggle_fullscreen(self):
        """Toggle fullscreen mode and reposition the ship."""
        self.settings.fullscreen = not self.settings.fullscreen
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        self.ship.screen = self.screen
        self.ship.screen_rect = self.screen.get_rect()
        
        # Adjust ship position to new screen size
        self.ship.center_ship()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _create_alien(self, alien_number, row_number, side_margin):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Position X now uses the calculated side margin for perfect centering.
        x = side_margin + 2 * alien_width * alien_number
        alien.rect.x = x

        # Sincronize x attribute with rect position.
        alien.x = float(alien.rect.x)

        # Y position calculation remains unchanged.
        y = self.sb.level_rect.bottom + alien_height + 2 * alien_height * row_number
        alien.rect.y = y
        
        self.aliens.add(alien)

    def _calculate_number_aliens_x(self, alien_width):
        """Calculate the number of aliens that fit in a row."""
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        return number_aliens_x

    def _calculate_side_margin(self, number_aliens_x, alien_width):
        """Calculate side margin for perfect centering."""
        number_aliens_x = number_aliens_x
        fleet_width = number_aliens_x * (2 * alien_width) - alien_width
        total_margin = self.settings.screen_width - fleet_width
        side_margin = total_margin / 2
        return side_margin
    
    def _calculate_space_for_rows(self, alien_height):
        """Available space for rows of aliens."""
        available_space_y = (self.settings.screen_height -
                        (self.sb.level_rect.height + alien_height) -
                        self.ship.rect.height)
        number_rows = available_space_y // (2 * alien_height)
        return number_rows

    def _create_fleet(self):
        """Create a full fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        number_aliens_x = self._calculate_number_aliens_x(alien_width)
        side_margin = self._calculate_side_margin(number_aliens_x, alien_width)
        number_rows = self._calculate_space_for_rows(alien_height)

        # Create the fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number, side_margin)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        # Check if the fleet is at an edge
        self._check_fleet_edges()
        
        # Update the positions of all aliens in the fleet.
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):  
            self._ship_hit()
        
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()    
            self.ship.center_ship()
            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
           
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
