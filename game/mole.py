# # game/mole.py
# import pygame

# class Mole:
#     def __init__(self, x, y, display):
#         self.radius = 50 # Used for collision detection
#         self.x, self.y = x, y
#         self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        
#         self.is_active = False
#         self.display = display
        
#         # New attributes for our Hitman theme
#         self.mole_type = None # Will be 'target' or 'civilian'
#         self.image = None # Will hold the loaded pygame image

#     def draw(self):
#         """Draws the mole's image if it is active."""
#         if self.is_active and self.image:
#             # Center the image on the mole's x, y coordinates
#             img_rect = self.image.get_rect(center=(self.x, self.y))
#             self.display.blit(self.image, img_rect)


# game/mole.py
import pygame
import os # Import os for path manipulation
import random

JITTER = 30

class Mole:
    radius = 50

    def __init__(self, x, y, display):
        self.base_x, self.base_y = x, y   # ← guardar la posición base
        self.x, self.y = x, y
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        
        self.is_active = False
        self.display = display
        
        self.mole_type = None 
        self.image = None 

    def set_image(self, original_image: pygame.Surface):
        """
        Sets the mole's image and masks it into a circle.
        Assumes original_image is already scaled to the correct size (2*radius x 2*radius).
        """
        # Create a new surface for the circular image, with alpha channel
        circle_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        
        # Draw a black anti-aliased circle onto the new surface
        # This will be our mask
        pygame.draw.circle(circle_surface, (255, 255, 255), (self.radius, self.radius), self.radius)
        
        # Blit the original image onto the circular surface, using the circle as a mask
        # This effectively cuts the image into a circle
        # The blend mode (pygame.BLEND_RGBA_MULT) multiplies the alpha channels
        # of the two surfaces. Where the mask is black (0 alpha), the image is transparent.
        # Where the mask is white (255 alpha), the image is fully visible.
        original_image.blit(circle_surface, (0, 0), None, pygame.BLEND_RGBA_MULT)
        
        self.image = original_image # Assign the now circular image
    
#    def draw(self):
#        if self.is_active and self.image:
#            img_rect = self.image.get_rect(center=(self.x, self.y))
#            self.display.blit(self.image, img_rect)

    def draw(self):
        if self.is_active and self.image:
            import random

            if not hasattr(self, "_offset"):  # genera jitter solo al aparecer
                dx = random.randint(-JITTER, JITTER)
                dy = random.randint(-JITTER, JITTER)

                # calcular nueva posición DESDE la base
                self.x = self.base_x + dx
                self.y = self.base_y + dy
                self.rect.center = (self.x, self.y)
                self._offset = (dx, dy)

            img_rect = self.image.get_rect(center=(self.x, self.y))
            self.display.blit(self.image, img_rect)
        else:
            if hasattr(self, "_offset"):
                del self._offset