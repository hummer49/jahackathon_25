# game/settings.py
import pygame

class Settings:
    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height
        self.title = "HIT-a-MOLE"
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 150, 0)
        self.RED = (150, 0, 0)
        self.BRIGHT_GREEN = (0, 255, 0)
        self.BRIGHT_RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        
        pygame.font.init()
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 50)
        self.font_small = pygame.font.Font(None, 36)
        
        self.clock = pygame.time.Clock()