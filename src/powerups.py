class PowerUp:
    def __init__(self, position, radius, color):
        self.position = list(position)
        self.radius = radius
        self.color = color

    def check_collision(self, ball):
        """Check if the power-up collides with the given ball."""
        dx = self.position[0] - ball.position[0]
        dy = self.position[1] - ball.position[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance <= self.radius + ball.radius
    
    def move(self, new_position):
        """Move the power-up to a new position."""
        self.position = list(new_position)
        
    def draw(self, screen):
        """Draw the power-up on the given screen."""
        import pygame
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)
        
class HealthUp(PowerUp):
    def __init__(self, position, radius, color, heal_amount = 1):
        super().__init__(position, radius, color)
        self.heal_amount = heal_amount

    # def handle_collision(self, ball):
    #     """Heal the ball upon collision."""
    #     if self.check_collision(ball):
    #         ball.heal(self.heal_amount)

class Spike(PowerUp):
    pass