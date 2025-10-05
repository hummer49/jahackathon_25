# game/mole.py
import pygame

class Mole:
    def __init__(self, x, y, display):
        self.radius = 50
        self.x, self.y = x, y
        self.is_active = False
        self.display = display

    def draw(self, red, black):
        color = red if self.is_active else black
        width = 0 if self.is_active else 3
        pygame.draw.circle(self.display, color, (self.x, self.y), self.radius, width)