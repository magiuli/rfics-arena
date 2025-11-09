import pygame
import physics as phys

class Arena:
    def __init__(self, left, top, width, height, border_thickness, border_color = (255, 255, 255), fighters = []):
        self.border = pygame.Rect(left, top, width, height)
        self.border_thickness = border_thickness
        self.border_color = border_color
        self.fighters = fighters

    def draw(self, screen):
        """Draw the arena borders on the given screen."""
        pygame.draw.rect(screen, self.border_color, self.border, self.border_thickness)

    def add_fighter(self, fighter):
        """Add a fighter to the arena."""
        self.fighters.append(fighter)

    def remove_dead_fighters(self):
        """Remove fighters with zero or less health from the arena."""
        self.fighters = [fighter for fighter in self.fighters if fighter.health > 0]

    def update_fighters(self, screen):
        """Update the state of all fighters in the arena."""
        for fighter in self.fighters:
            fighter.move()
            fighter.check_wall_collision(self)
            fighter.draw(screen)

        for i in range(len(self.fighters)):
            for j in range(i + 1, len(self.fighters)):
                phys.handle_ball_collision(self.fighters[i], self.fighters[j])

        self.remove_dead_fighters()