import pygame

# GLOBAL VARIABLES


colors = {
    "BLACK" : (0, 0, 0),
    "GREY" : (125, 125, 125),
    "RED" : (255, 0, 0),
    "BLUE" : (30, 144, 255),
    "WHITE" : (255, 255, 255),
}

settings = {
    "screen_width": 800,
    "screen_height": 600,
}


def draw_start_screen(screen):
    """Draws the start screen with instructions."""
    screen.fill(colors["BLUE"])
    font = pygame.font.SysFont('Arial', 40)
    title_text = font.render('My Circle Game', True, colors["WHITE"])
    instr_text = font.render('Press SPACE to Start', True, colors["WHITE"])
    
    # Center the text
    title_rect = title_text.get_rect(center=(settings["screen_width"] // 2, settings["screen_height"] // 2 - 50))
    instr_rect = instr_text.get_rect(center=(settings["screen_width"] // 2, settings["screen_height"] // 2 + 50))
    
    screen.blit(title_text, title_rect)
    screen.blit(instr_text, instr_rect)

def draw_game_screen_l1(screen):
    """Draws the main game screen with the three circles."""
    screen.fill(colors["BLACK"])
    
    # Circle properties (same as before)
    circle_radius = 50
    circle_y = settings["screen_height"] // 2
    spacing = 100
    circle_x1 = settings["screen_width"] // 2 - circle_radius - spacing
    circle_x2 = settings["screen_width"] // 2
    circle_x3 = settings["screen_width"] // 2 + circle_radius + spacing

    # Draw the three circles
    pygame.draw.circle(screen, colors["RED"], (circle_x1, circle_y), circle_radius)
    pygame.draw.circle(screen, colors["RED"], (circle_x2, circle_y), circle_radius)
    pygame.draw.circle(screen, colors["RED"], (circle_x3, circle_y), circle_radius)









