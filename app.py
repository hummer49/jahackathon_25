# # V1
# import pygame
# import random
# import sys

# class Settings:
#     def __init__(self, width: int = 800, height: int = 600):
#         self.width = width
#         self.height = height
#         self.title = "HIT-a-MOLE"
#         self.WHITE = (255, 255, 255)
#         self.BLACK = (0, 0, 0)
#         self.RED = (255, 0, 0)
#         self.BLUE = (0, 0, 255)
#         self.num_holes = 5 # Number of holes for moles to appear in
#         pygame.font.init() # Initialize font module
#         self.font_0 = pygame.font.Font(None, 36)
#         self.clock = pygame.time.Clock()

# class Player:
#     def __init__(self, name: str = "Agent 48"):
#         self.name = name
#         self.score = 0 # Direct access is fine for a simple game

# class Mole:
#     def __init__(self, x, y, display):
#         self.radius = 50
#         self.x = x
#         self.y = y
#         self.is_active = False # Is the mole "up"?
#         self.display = display

#     def draw(self, red, black):
#         # Draw red if active, otherwise black
#         color = red if self.is_active else black
#         width = 0 if self.is_active else 3 # 0 for filled, 3 for outline
#         pygame.draw.circle(self.display, color, (self.x, self.y), self.radius, width)

# def main():
#     # Initialize game
#     pygame.init()

#     # Setup the display and player
#     settings = Settings()
#     player = Player()
#     display = pygame.display.set_mode(size=(settings.width, settings.height))
#     pygame.display.set_caption(settings.title)

#     # --- Create the mole holes ONCE ---
#     moles = []
#     for i in range(settings.num_holes):
#         x_pos = (i + 1) * (settings.width // (settings.num_holes + 1))
#         y_pos = settings.height // 2
#         moles.append(Mole(x_pos, y_pos, display))

#     # --- Game state variables ---
#     active_mole = None
#     round_time_limit = 1000  # 1 second
#     round_start_time = 0

#     def start_new_round():
#         """Resets the previous mole and activates a new random one."""
#         nonlocal active_mole, round_start_time
        
#         # Deactivate the previous mole if one exists
#         if active_mole:
#             active_mole.is_active = False
        
#         # Activate a new random mole
#         active_mole = random.choice(moles)
#         active_mole.is_active = True
        
#         # Start the timer for the new round
#         round_start_time = pygame.time.get_ticks()

#     # Start the first round
#     start_new_round()

#     # Main game loop
#     while True:
#         # --- Event Handling ---
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 distance = ((mouse_x - active_mole.x) ** 2 + (mouse_y - active_mole.y) ** 2) ** 0.5

#                 # Check if the click was on the active mole
#                 if distance <= active_mole.radius:
#                     player.score += 1
#                 else: # Player missed
#                     player.score -= 1
                
#                 # Regardless of hit or miss, start the next round
#                 start_new_round()

#         # --- Game Logic ---
#         # Check if the time for the current round has expired
#         elapsed_time = pygame.time.get_ticks() - round_start_time
#         if elapsed_time > round_time_limit:
#             player.score -= 1 # Penalize for being too slow
#             start_new_round()

#         # --- Drawing ---
#         display.fill(settings.BLUE)

#         for mole in moles:
#             mole.draw(red=settings.RED, black=settings.BLACK)
        
#         score_text = settings.font_0.render(f"Score: {player.score}", True, settings.WHITE)
#         display.blit(score_text, (10, 10))

#         pygame.display.flip()
#         settings.clock.tick(60)

# if __name__ == "__main__":
#     main()

#V2
import pygame
import random
import sys

class Settings:
    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height
        self.title = "HIT-a-MOLE"
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.num_holes = 5
        pygame.font.init()
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

class Player:
    def __init__(self, name: str = "Agent 48", lives: int = 3):
        self.name = name
        self.start_lives = lives
        self.score = 0
        self.lives = self.start_lives
    
    def reset(self):
        """Resets score and lives for a new game."""
        self.score = 0
        self.lives = self.start_lives

class Mole:
    def __init__(self, x, y, display):
        self.radius = 50
        self.x = x
        self.y = y
        self.is_active = False
        self.display = display

    def draw(self, red, black):
        color = red if self.is_active else black
        width = 0 if self.is_active else 3
        pygame.draw.circle(self.display, color, (self.x, self.y), self.radius, width)

def draw_home_screen(display, settings):
    display.fill(settings.BLACK)
    title_text = settings.font_large.render(settings.title, True, settings.WHITE)
    prompt_text = settings.font_medium.render("Click anywhere to start", True, settings.WHITE)
    
    title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 50))
    prompt_rect = prompt_text.get_rect(center=(settings.width / 2, settings.height / 2 + 20))
    
    display.blit(title_text, title_rect)
    display.blit(prompt_text, prompt_rect)

def draw_game_screen(display, settings, moles, player):
    display.fill(settings.BLUE)
    for mole in moles:
        mole.draw(red=settings.RED, black=settings.BLACK)
    
    score_text = settings.font_medium.render(f"Score: {player.score}", True, settings.WHITE)
    lives_text = settings.font_medium.render(f"Lives: {player.lives}", True, settings.WHITE)
    
    display.blit(score_text, (10, 10))
    display.blit(lives_text, (settings.width - 120, 10))

def draw_game_over_screen(display, settings, player):
    display.fill(settings.BLACK)
    title_text = settings.font_large.render("GAME OVER", True, settings.RED)
    score_text = settings.font_medium.render(f"Final Score: {player.score}", True, settings.WHITE)
    prompt_text = settings.font_medium.render("Click to return to menu", True, settings.WHITE)
    
    title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 50))
    score_rect = score_text.get_rect(center=(settings.width / 2, settings.height / 2 + 20))
    prompt_rect = prompt_text.get_rect(center=(settings.width / 2, settings.height / 2 + 60))
    
    display.blit(title_text, title_rect)
    display.blit(score_text, score_rect)
    display.blit(prompt_text, prompt_rect)

def main():
    pygame.init()
    settings = Settings()
    player = Player(lives=3)
    display = pygame.display.set_mode(size=(settings.width, settings.height))
    pygame.display.set_caption(settings.title)

    moles = []
    for i in range(settings.num_holes):
        x_pos = (i + 1) * (settings.width // (settings.num_holes + 1))
        y_pos = settings.height // 2
        moles.append(Mole(x_pos, y_pos, display))

    active_mole = None
    round_time_limit = 1000
    round_start_time = 0
    game_state = "home"

    def start_new_round():
        nonlocal active_mole, round_start_time
        if active_mole:
            active_mole.is_active = False
        
        active_mole = random.choice(moles)
        active_mole.is_active = True
        round_start_time = pygame.time.get_ticks()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "home":
                    player.reset()
                    start_new_round()
                    game_state = "playing"

                elif game_state == "playing":
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    distance = ((mouse_x - active_mole.x) ** 2 + (mouse_y - active_mole.y) ** 2) ** 0.5

                    if distance <= active_mole.radius:
                        player.score += 1
                    else:
                        # This is now the ONLY way to lose a life
                        player.lives -= 1
                    
                    if player.lives > 0:
                        start_new_round()
                    else:
                        game_state = "game_over"
                
                elif game_state == "game_over":
                    game_state = "home"

        if game_state == "playing":
            # Check if time expired
            elapsed_time = pygame.time.get_ticks() - round_start_time
            if elapsed_time > round_time_limit:
                # --- CHANGE HERE ---
                # No more penalty! Just start a new round.
                start_new_round()
            
            draw_game_screen(display, settings, moles, player)
        
        elif game_state == "home":
            draw_home_screen(display, settings)
        
        elif game_state == "game_over":
            draw_game_over_screen(display, settings, player)

        pygame.display.flip()
        settings.clock.tick(60)

if __name__ == "__main__":
    main()