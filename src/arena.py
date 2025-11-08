import pygame

class Arena:
    def __init__(self, left, top, width, height, border_thickness, border_color = (255, 255, 255)):
        self.border = pygame.Rect(left, top, width, height)
        self.border_thickness = border_thickness
        self.border_color = border_color

    def draw(self, screen):
        """Draw the arena borders on the given screen."""
        pygame.draw.rect(screen, self.border_color, self.border, self.border_thickness)

    