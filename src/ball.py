import pygame
import config as cfg

class Ball:
    def __init__(self, position, radius, color, velocity = (0, 0), mass = 1.0, team = None):
        self.position = list(position)
        self.radius = radius
        self.color = color
        self.velocity = list(velocity)
        self.mass = mass
        self.team = team

    def move(self):
        """Update the ball's position based on its velocity."""
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def draw(self, screen):
        """Draw the ball on the given screen."""
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

    def check_wall_collision(self, arena):
        """Check and handle collisions with the arena borders."""
        # left
        if self.position[0] - self.radius <= arena.border.left + arena.border_thickness:
            self.position[0] = arena.border.left + self.radius + arena.border_thickness
            self.velocity[0] *= -1
        # right
        if self.position[0] + self.radius >= arena.border.right - arena.border_thickness:
            self.position[0] = arena.border.right - self.radius - arena.border_thickness
            self.velocity[0] *= -1
        # top
        if self.position[1] - self.radius <= arena.border.top + arena.border_thickness:
            self.position[1] = arena.border.top + self.radius + arena.border_thickness
            self.velocity[1] *= -1
        # bottom
        if self.position[1] + self.radius >= arena.border.bottom - arena.border_thickness:
            self.position[1] = arena.border.bottom - self.radius - arena.border_thickness
            self.velocity[1] *= -1