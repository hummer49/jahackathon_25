# # app.py
# import pygame
# import sys
# import random

# # Import all the components from your game package
# from game.settings import Settings
# from game.player import Player
# from game.level import Level
# from game.mole import Mole
# import game.screens as screens

# def main():
#     pygame.init()
#     settings = Settings()
#     player = Player()
#     display = pygame.display.set_mode(size=(settings.width, settings.height))
#     pygame.display.set_caption(settings.title)

#     STARTING_LIVES = 3
#     MAX_LEVELS = 7 # Last level is index 6
    
#     current_level, moles, active_mole = None, [], None
#     round_time_limit, round_start_time = 1000, 0
#     game_state = "home"

#     button_w, button_h = 200, 70
#     button_y = settings.height / 2 + 80
#     continue_button = pygame.Rect(settings.width/4 - button_w/2, button_y, button_w, button_h)
#     quit_button = pygame.Rect(settings.width*3/4 - button_w/2, button_y, button_w, button_h)

#     def setup_level(level_obj):
#         nonlocal moles
#         moles.clear()
#         for i in range(level_obj.holes):
#             x = (i + 1) * (settings.width // (level_obj.holes + 1))
#             moles.append(Mole(x, settings.height / 2, display))

#     def start_new_round():
#         nonlocal active_mole, round_start_time
#         if active_mole: active_mole.is_active = False
#         if moles: active_mole = random.choice(moles); active_mole.is_active = True
#         round_start_time = pygame.time.get_ticks()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit(); sys.exit()

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if game_state == "home":
#                     player.reset()
#                     current_level = Level(n_level=0, starting_lives=STARTING_LIVES)
#                     setup_level(current_level)
#                     start_new_round()
#                     game_state = "playing"
                
#                 elif game_state == "playing":
#                     mouse_x, mouse_y = pygame.mouse.get_pos()
#                     dist = ((mouse_x - active_mole.x)**2 + (mouse_y - active_mole.y)**2)**0.5

#                     if dist <= active_mole.radius:
#                         player.total_score += 1
#                         current_level.increment_hits()
                        
#                         if current_level.is_complete():
#                             if current_level.n_level + 1 >= MAX_LEVELS:
#                                 game_state = "win"
#                             else:
#                                 game_state = "level_complete"
#                         else:
#                             start_new_round()
#                     else:
#                         current_level.lose_life()
#                         if not current_level.has_lives():
#                             game_state = "game_over"
#                         else:
#                             start_new_round()
                
#                 # elif game_state == "level_complete":
#                 #     mouse_pos = event.pos
#                 #     if continue_button.collidepoint(mouse_pos):
#                 #         next_level_num = current_level.n_level + 1
#                 #         current_level = Level(n_level=next_level_num, starting_lives=STARTING_LIVES)
#                 #         setup_level(current_level)
#                 #         start_new_round()
#                 #         game_state = "playing"
#                 #     elif quit_button.collidepoint(mouse_pos):
#                 #         game_state = "home"
#                 # ===
#                 elif game_state == "level_complete":
#                     mouse_pos = event.pos
#                     if continue_button.collidepoint(mouse_pos):
#                         next_level_num = current_level.n_level + 1
                        
#                         # Update the last_level_played for the current session
#                         player.last_level_played = next_level_num

#                         current_level = Level(n_level=next_level_num, starting_lives=STARTING_LIVES)
#                         setup_level(current_level)
#                         start_new_round()
#                         game_state = "playing"
#                     elif quit_button.collidepoint(mouse_pos):
#                         game_state = "home"
#                 # ===
#                 elif game_state in ["game_over", "win"]:
#                     game_state = "home"

#         if game_state == "playing":
#             if pygame.time.get_ticks() - round_start_time > round_time_limit:
#                 start_new_round()
#             screens.draw_game_screen(display, settings, moles, player, current_level)
        
#         elif game_state == "home":
#             screens.draw_home_screen(display, settings)
        
#         elif game_state == "level_complete":
#             screens.draw_level_complete_screen(display, settings, player, continue_button, quit_button)

#         elif game_state == "game_over":
#             screens.draw_game_over_screen(display, settings, player)
            
#         elif game_state == "win":
#             screens.draw_win_screen(display, settings, player)

#         pygame.display.flip()
#         settings.clock.tick(60)

# if __name__ == "__main__":
#     main()

# app.py
import pygame
import sys
import random

# Import all the components from your game package
from game.settings import Settings
from game.player import Player
from game.level import Level
from game.mole import Mole
import game.screens as screens
# Import TARGETS and CIVILIAN_MOLES for a potential quick reference or more robust error handling
from game.missions import TARGETS, CIVILIAN_MOLES

def main():
    pygame.init()
    settings = Settings()
    player = Player()
    display = pygame.display.set_mode(size=(settings.width, settings.height))
    pygame.display.set_caption(settings.title)

    STARTING_LIVES = 3
    # MAX_LEVELS should match the number of entries in TARGETS
    MAX_LEVELS = len(TARGETS) 
    
    # --- State variables ---
    current_level, moles, active_mole = None, [], None
    round_time_limit, round_start_time = 1000, 0
    game_state = "home" # Possible states: "home", "briefing", "playing", "level_complete", "game_over", "win"

    # --- Button Rects for various screens ---
    button_w, button_h = 200, 70
    button_y_offset = 80 # A common offset for buttons from the center
    
    # Buttons for Level Complete screen
    continue_button = pygame.Rect(settings.width/4 - button_w/2, settings.height / 2 + button_y_offset, button_w, button_h)
    quit_button = pygame.Rect(settings.width*3/4 - button_w/2, settings.height / 2 + button_y_offset, button_w, button_h)
    
    # Button for Mission Briefing screen
    start_mission_button = pygame.Rect(settings.width/2 - button_w/2, settings.height / 2 + button_y_offset, button_w, button_h)

    # --- NEW: Image Loading Cache with Circular Masking ---
    loaded_images = {}
    def get_circular_image(path):
        if path not in loaded_images:
            try:
                # Load the original image
                image_original = pygame.image.load(path).convert_alpha()
                # Scale it to the desired size (2*radius x 2*radius)
                scaled_image = pygame.transform.smoothscale(image_original, (Mole(0,0,None).radius * 2, Mole(0,0,None).radius * 2))
                
                # Create a transparent surface for the circular mask
                mask_surface = pygame.Surface(scaled_image.get_size(), pygame.SRCALPHA)
                # Draw an opaque white circle on the mask surface
                pygame.draw.circle(mask_surface, (255, 255, 255, 255), (Mole(0,0,None).radius, Mole(0,0,None).radius), Mole(0,0,None).radius)
                
                # Apply the mask to the scaled image using BLEND_RGBA_MULT
                scaled_image.blit(mask_surface, (0, 0), None, pygame.BLEND_RGBA_MULT)

                loaded_images[path] = scaled_image
            except pygame.error as e:
                print(f"Error loading image {path}: {e}")
                # Provide a fallback (e.g., a red circle) if image fails to load
                fallback_image = pygame.Surface((Mole(0,0,None).radius * 2, Mole(0,0,None).radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(fallback_image, settings.RED, (Mole(0,0,None).radius, Mole(0,0,None).radius), Mole(0,0,None).radius)
                loaded_images[path] = fallback_image

        return loaded_images[path]

    # --- UPDATED: Level Setup ---
    def setup_level(level_obj):
        nonlocal moles
        moles.clear()
        
        # Ensure target data exists for this level
        if level_obj.target_data is None:
            print(f"Error: No target data for level {level_obj.n_level}. Game cannot proceed.")
            # Handle gracefully, e.g., transition to game_over or home screen
            pygame.quit(); sys.exit() 
            
        # Get target image (now circular)
        target_img_surface = get_circular_image(level_obj.target_data["image_path"])
        # Get civilian images (now circular)
        civilian_img_surfaces = [get_circular_image(p) for p in level_obj.civilian_images]
        
        # Create the moles (holes/positions)
        for i in range(level_obj.holes):
            x = (i + 1) * (settings.width // (level_obj.holes + 1))
            moles.append(Mole(x, settings.height / 2, display))
            
        # Assign one mole to be the target
        target_mole = random.choice(moles)
        target_mole.mole_type = "target"
        target_mole.image = target_img_surface 
        
        # Assign the rest to be civilians with random civilian images
        for mole in moles:
            if mole.mole_type is None: # If not yet assigned (i.e., not the target)
                mole.mole_type = "civilian"
                # Ensure we have civilian images to choose from
                if civilian_img_surfaces:
                    mole.image = random.choice(civilian_img_surfaces)
                else:
                    print("Warning: No civilian images available. Using fallback red circle.")
                    fallback_image = pygame.Surface((Mole(0,0,None).radius * 2, Mole(0,0,None).radius * 2), pygame.SRCALPHA)
                    pygame.draw.circle(fallback_image, settings.RED, (Mole(0,0,None).radius, Mole(0,0,None).radius), Mole(0,0,None).radius)
                    mole.image = fallback_image


    def start_new_round():
        nonlocal active_mole, round_start_time
        # Deactivate previous active mole if any
        if active_mole: active_mole.is_active = False
        
        # Choose a new random mole to activate
        if moles: 
            active_mole = random.choice(moles)
            active_mole.is_active = True
        else:
            print("Warning: No moles to activate for the round!")
        round_start_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "home":
                    player.reset()
                    current_level = Level(n_level=0, starting_lives=STARTING_LIVES)
                    game_state = "briefing" # Transition to briefing screen
                
                # --- NEW: Briefing State Logic ---
                elif game_state == "briefing":
                    if start_mission_button.collidepoint(event.pos):
                        setup_level(current_level) # Setup moles for the level after briefing
                        start_new_round()
                        game_state = "playing" # Start playing

                elif game_state == "playing":
                    # --- UPDATED: Hitman Logic for clicks ---
                    # Check if the click was within the active mole's bounding box
                    if active_mole and active_mole.rect.collidepoint(event.pos):
                        if active_mole.mole_type == 'target':
                            player.total_score += 1
                            current_level.increment_hits()
                            
                            if current_level.is_complete():
                                # Update player's highest completed level record
                                if current_level.n_level > player.max_level_reached:
                                    player.max_level_reached = current_level.n_level

                                if current_level.n_level + 1 >= MAX_LEVELS:
                                    game_state = "win" # Game won!
                                else:
                                    game_state = "level_complete" # Proceed to next level
                            else:
                                start_new_round() # Continue current level
                        elif active_mole.mole_type == 'civilian':
                            # Penalty for hitting a civilian!
                            current_level.lose_life()
                            if not current_level.has_lives():
                                game_state = "game_over" # No lives left
                            else:
                                start_new_round() # Continue current level with fewer lives
                    else: # Player missed the active mole (either hit empty space or wrong mole)
                        current_level.lose_life()
                        if not current_level.has_lives():
                            game_state = "game_over" # No lives left
                        else:
                            start_new_round() # Continue current level with fewer lives
                
                elif game_state == "level_complete":
                    if continue_button.collidepoint(event.pos):
                        next_level_num = current_level.n_level + 1
                        player.last_level_played = next_level_num # Track level reached in this run
                        current_level = Level(n_level=next_level_num, starting_lives=STARTING_LIVES)
                        game_state = "briefing" # Go to briefing for next mission
                    elif quit_button.collidepoint(event.pos):
                        game_state = "home" # Go back to home screen
                
                elif game_state in ["game_over", "win"]:
                    game_state = "home" # Return to home screen from game over/win

        # --- State-based Drawing ---
        if game_state == "playing":
            # Check for round time limit
            if pygame.time.get_ticks() - round_start_time > round_time_limit:
                start_new_round() # Mole disappears if not hit in time
            screens.draw_game_screen(display, settings, moles, player, current_level)
        
        elif game_state == "home":
            screens.draw_home_screen(display, settings, player) # Pass player for highest level
        
        # --- NEW: Draw Briefing Screen ---
        elif game_state == "briefing":
            screens.draw_briefing_screen(display, settings, current_level, start_mission_button)
        
        elif game_state == "level_complete":
            # Correctly passing 'current_level' to draw_level_complete_screen
            screens.draw_level_complete_screen(display, settings, player, current_level, continue_button, quit_button)

        elif game_state == "game_over":
            screens.draw_game_over_screen(display, settings, player) # Pass player for level reached
            
        elif game_state == "win":
            screens.draw_win_screen(display, settings, player)

        pygame.display.flip()
        settings.clock.tick(60)

if __name__ == "__main__":
    main()