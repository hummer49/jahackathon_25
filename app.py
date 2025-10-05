# import sys
# import pygame
# import random
# import sys



# class Settings:
#     def __init__(
#         self, 
#         height:int=800, 
#         width:int=600
#     ):
#         self.height = height
#         self.width = width
#         self.title = "HIT-a-MOLE"
#         self.WHITE = (255, 255, 255)
#         self.BLACK = (0, 0, 0)
#         self.RED = (255, 0, 0)
#         self.BLUE = (0, 0, 255)
#         self.font_0 = pygame.font.Font(None, 36)
#         self.clock = pygame.time.Clock()


# class Player:
#     def __init__(
#         self,
#         name:str = "Agente 48"
#     ):
#         self.name = name
#         self.__score = 0
#         self.__max_level = 0
#     def set_score(self, n:int):
#         self.__score = n
#     def get_score(self):
#         return self.__score
#     def set_max_level(self, n:int):
#         self.__max_level = n
#     def get_max_level(self):
#         return self.__max_level
    
# class Circle:
#     def __init__(
#         self,
#         filled,
#         x,
#         y,
#         display
#     ):
#         self.radius = 50
#         self.x = x
#         self.y = y
#         self.filled = filled
#         self.display = display
#     def draw(self, red, black):
#         color = red if self.filled else black
#         pygame.draw.circle(
#             self.display,
#             color,
#             (self.x, self.y),
#             self.radius,
#             3 if not self.filled else 0
#         )

# def main():
#     #initialize game
#     pygame.init()

#     #initialize the player
#     player = Player()

#     #setup the display
#     settings = Settings()
#     display = pygame.display.set_mode(
#         size=(settings.width, settings.height)
#     )
#     pygame.display.set_caption(settings.title)

    
#     round_time = 1000
#     start_time = None
#     # ===
#     #create the circles
#     circles = []
#     for i in range(4):
#         circles.append(
#             Circle(
#                 filled=False,
#                 x=(i+1)*(settings.width//6),
#                 y=settings.height//2,
#                 display=display
#             )
#         )
#     for i in range(5):
#         circles.append(
#             Circle(
#                 filled=True,
#                 # x=random.choice((i+1)*(settings.width//6)),
#                 x=random.choice([(i + 1) * (settings.width // 6) for i in range(5)]),
#                 y=settings.height//2,
#                 display=display
#             )
#         )
#     # ===

#     # main game loop
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#                 break
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if start_time is not None:
#                     elapsed_time = pygame.time.get_ticks() - start_time
#                     mouse_x, mouse_y = pygame.mouse.get_pos()
#                     clicked_circle = None
#                     for circle in circles:
#                         distance = ((mouse_x - circle.x) ** 2 + (mouse_y - circle.y) ** 2) ** 0.5
#                         if distance <= circle.radius and circle.filled:
#                             clicked_circle = circle
#                             break
#                     if clicked_circle is not None and elapsed_time <= round_time:
#                         player.set_score(player.get_score()+1)
#                     else:
#                         player.set_score(player.get_score()-1)
#                 start_time = None
#                 # ===
#                 #create the circles
#                 circles = []
#                 for i in range(4):
#                     circles.append(
#                         Circle(
#                             filled=False,
#                             x=(i+1)*(settings.width//6),
#                             y=settings.height//2,
#                             display=display
#                         )
#                     )
#                 for i in range(5):
#                     circles.append(
#                         Circle(
#                             filled=True,
#                             # x=random.choice((i+1)*(settings.width//6)),
#                             x=random.choice([(i + 1) * (settings.width // 6) for i in range(5)]),
#                             y=settings.height//2,
#                             display=display
#                         )
#                     )
#         display.fill(settings.BLUE)
#         for circle in circles:
#             circle.draw(red=settings.RED, black=settings.BLACK)
#         score_text = settings.font_0.render(f"Score: {player.get_score()}", True, settings.WHITE)
#         display.blit(score_text, (10,10))

#         pygame.display.flip()
#         settings.clock.tick(60)
#         if start_time is None and circles[-1].filled:
#             start_time = pygame.time.get_ticks()


# # END main

# if __name__=="__main__":
#     main()


# V1
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
        self.num_holes = 5 # Number of holes for moles to appear in
        pygame.font.init() # Initialize font module
        self.font_0 = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

class Player:
    def __init__(self, name: str = "Agent 48"):
        self.name = name
        self.score = 0 # Direct access is fine for a simple game

class Mole:
    def __init__(self, x, y, display):
        self.radius = 50
        self.x = x
        self.y = y
        self.is_active = False # Is the mole "up"?
        self.display = display

    def draw(self, red, black):
        # Draw red if active, otherwise black
        color = red if self.is_active else black
        width = 0 if self.is_active else 3 # 0 for filled, 3 for outline
        pygame.draw.circle(self.display, color, (self.x, self.y), self.radius, width)

def main():
    # Initialize game
    pygame.init()

    # Setup the display and player
    settings = Settings()
    player = Player()
    display = pygame.display.set_mode(size=(settings.width, settings.height))
    pygame.display.set_caption(settings.title)

    # --- Create the mole holes ONCE ---
    moles = []
    for i in range(settings.num_holes):
        x_pos = (i + 1) * (settings.width // (settings.num_holes + 1))
        y_pos = settings.height // 2
        moles.append(Mole(x_pos, y_pos, display))

    # --- Game state variables ---
    active_mole = None
    round_time_limit = 1000  # 1 second
    round_start_time = 0

    def start_new_round():
        """Resets the previous mole and activates a new random one."""
        nonlocal active_mole, round_start_time
        
        # Deactivate the previous mole if one exists
        if active_mole:
            active_mole.is_active = False
        
        # Activate a new random mole
        active_mole = random.choice(moles)
        active_mole.is_active = True
        
        # Start the timer for the new round
        round_start_time = pygame.time.get_ticks()

    # Start the first round
    start_new_round()

    # Main game loop
    while True:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                distance = ((mouse_x - active_mole.x) ** 2 + (mouse_y - active_mole.y) ** 2) ** 0.5

                # Check if the click was on the active mole
                if distance <= active_mole.radius:
                    player.score += 1
                else: # Player missed
                    player.score -= 1
                
                # Regardless of hit or miss, start the next round
                start_new_round()

        # --- Game Logic ---
        # Check if the time for the current round has expired
        elapsed_time = pygame.time.get_ticks() - round_start_time
        if elapsed_time > round_time_limit:
            player.score -= 1 # Penalize for being too slow
            start_new_round()

        # --- Drawing ---
        display.fill(settings.BLUE)

        for mole in moles:
            mole.draw(red=settings.RED, black=settings.BLACK)
        
        score_text = settings.font_0.render(f"Score: {player.score}", True, settings.WHITE)
        display.blit(score_text, (10, 10))

        pygame.display.flip()
        settings.clock.tick(60)

if __name__ == "__main__":
    main()