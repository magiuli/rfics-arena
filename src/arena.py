import pygame
import physics as phys

class Arena:
    def __init__(self, left, top, width, height, border_thickness, border_color = (255, 255, 255), fighters = []):
        self.border = pygame.Rect(left, top, width, height)
        self.border_thickness = border_thickness
        self.border_color = border_color
        self.fighters = fighters
        self.health_ups = []
        self.spikes = []

    def draw(self, screen):
        """Draw the arena borders on the given screen."""
        pygame.draw.rect(screen, self.border_color, self.border, self.border_thickness)

    def add_fighter(self, fighter):
        """Add a fighter to the arena."""
        self.fighters.append(fighter)

    def remove_dead_fighters(self):
        """Remove fighters with zero or less health from the arena."""
        self.fighters = [fighter for fighter in self.fighters if fighter.health > 0]

    def generate_random_position(self, radius):
        """Generate a random position within the arena that accounts for the given radius."""
        import random
        x = random.randint(self.border.left + self.border_thickness + radius,
                           self.border.right - self.border_thickness - radius)
        y = random.randint(self.border.top + self.border_thickness + radius,
                           self.border.bottom - self.border_thickness - radius)
        
        # Ensure the position does not overlap with existing fighters
        for fighter in self.fighters:
            dx = x - fighter.position[0]
            dy = y - fighter.position[1]
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance <= radius + fighter.radius:
                return self.generate_random_position(radius)
            
        return (x, y)
    
    def add_health_up(self):
        """Add a health power-up at a random position in the arena."""
        from powerups import HealthUp
        import config as cfg

        position = self.generate_random_position(cfg.POWERUP_RADIUS)
        health_up = HealthUp(position, cfg.POWERUP_RADIUS, cfg.RED)
        self.health_ups.append(health_up)

    def handle_health_up_collision(self, ball, health_up):
        """Handle collision between a ball and a health power-up."""
        ball.heal(health_up.heal_amount)
        health_up.move(self.generate_random_position(health_up.radius))

    def check_health_up_collisions(self):
        """Check for collisions between fighters and health power-ups."""
        for fighter in self.fighters:
            for health_up in self.health_ups:
                if health_up.check_collision(fighter):
                    self.handle_health_up_collision(fighter, health_up)

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

    def update_powerups(self, screen):
        """Update the state of all power-ups in the arena."""
        for health_up in self.health_ups:
            health_up.draw(screen)
        
        self.check_health_up_collisions()

    def update(self, screen):
        """Update the arena state."""
        self.update_fighters(screen)
        self.update_powerups(screen)