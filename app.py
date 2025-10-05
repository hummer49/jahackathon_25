# app.py
import pygame
import sys
import random
import logging

# Import all the components from your game package
from game.settings import Settings
from game.player import Player
from game.level import Level
from game.mole import Mole
import game.screens as screens
# Import LEVEL_THEMES for the new theme-based system
from game.missions import LEVEL_THEMES

# Configure logging for game events
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('game_events.log'),
        logging.StreamHandler()  # Also log to console
    ]
)
logger = logging.getLogger(__name__)

def main():
    pygame.init()
    settings = Settings()
    player = Player()
    display = pygame.display.set_mode(size=(settings.width, settings.height))
    pygame.display.set_caption(settings.title)

    STARTING_LIVES = 3
    # MAX_LEVELS should match the number of entries in LEVEL_THEMES
    MAX_LEVELS = len(LEVEL_THEMES) 
    
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
    
    # Hint button for game screen (bottom right)
    hint_button = pygame.Rect(settings.width - 120, settings.height - 50, 100, 40)
    
    # Hint dialog state
    show_hint_dialog = False

    # --- Image Loading Cache with Circular Masking and Background Support ---
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
            except (pygame.error, FileNotFoundError) as e:
                print(f"WARNING: Missing mole image asset '{path}': {e}")
                print(f"         Using red circle fallback. Please add the missing image file.")
                # Provide a fallback (e.g., a red circle) if image fails to load
                fallback_image = pygame.Surface((Mole(0,0,None).radius * 2, Mole(0,0,None).radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(fallback_image, settings.RED, (Mole(0,0,None).radius, Mole(0,0,None).radius), Mole(0,0,None).radius)
                loaded_images[path] = fallback_image

        return loaded_images[path]
    
    def get_background_image(path):
        if path not in loaded_images:
            try:
                # Load background and scale to screen size
                background_original = pygame.image.load(path).convert()
                background_scaled = pygame.transform.smoothscale(background_original, (settings.width, settings.height))
                loaded_images[path] = background_scaled
            except (pygame.error, FileNotFoundError) as e:
                print(f"WARNING: Missing background image asset '{path}': {e}")
                print(f"         Using blue background fallback. Please add the missing image file.")
                # Fallback: solid color background
                fallback_bg = pygame.Surface((settings.width, settings.height))
                fallback_bg.fill(settings.BLUE)
                loaded_images[path] = fallback_bg
        return loaded_images[path]

    # --- UPDATED: Level Setup with Theme System ---
    def setup_level(level_obj):
        nonlocal moles
        moles.clear()
        
        # Ensure theme data exists for this level
        if level_obj.theme_data is None:
            print(f"ERROR: No theme data for level {level_obj.n_level}. Game cannot proceed.")
            # Handle gracefully, e.g., transition to game_over or home screen
            pygame.quit(); sys.exit() 
            
        # Load background image for this theme
        level_obj.background_surface = get_background_image(level_obj.background_image)
        
        # Get target image (now circular)
        target_img_surface = get_circular_image(level_obj.target_data["image_path"])
        # Get civilian images (now circular)
        civilian_img_surfaces = [get_circular_image(p) for p in level_obj.civilian_images]

        # guardar:
        level_obj._target_img_surface = target_img_surface
        level_obj._civilian_img_surfaces = civilian_img_surfaces
        
        # Create the moles (holes/positions)
        if 0 <= level_obj.n_level < 2:
            cols, rows = 2, 2
        elif level_obj.n_level < 4:
            cols, rows = 3, 2
        else:
            cols, rows = 3, 3

        level_obj.holes = cols * rows

        moles.clear()
        for r in range(rows):
            y = (r + 1) * (settings.height // (rows + 1))
            for c in range(cols):
                x = (c + 1) * (settings.width // (cols + 1))
                moles.append(Mole(x, y, display))
            
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
                    print("WARNING: No civilian images available for this theme. Using fallback red circle.")
                    fallback_image = pygame.Surface((Mole(0,0,None).radius * 2, Mole(0,0,None).radius * 2), pygame.SRCALPHA)
                    pygame.draw.circle(fallback_image, settings.RED, (Mole(0,0,None).radius, Mole(0,0,None).radius), Mole(0,0,None).radius)
                    mole.image = fallback_image


    def start_new_round(level_obj):
        nonlocal active_mole, round_start_time
        if active_mole:
            active_mole.is_active = False

        import random

        # --- Evitar repetir el mismo topo ---
        if active_mole:
            choices = [m for m in moles if m != active_mole]
        else:
            choices = moles
        active_mole = random.choice(choices)
        # ------------------------------------

        # 1/N de probabilidad de que sea target (o ajustá la probabilidad)
        if random.random() < (1 / len(moles)):
            active_mole.mole_type = "target"
            active_mole.image = level_obj._target_img_surface
        else:
            active_mole.mole_type = "civilian"
            if level_obj._civilian_img_surfaces:
                active_mole.image = random.choice(level_obj._civilian_img_surfaces)

        active_mole.is_active = True
        round_start_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "home":
                    player.reset()
                    current_level = Level(n_level=0, starting_lives=STARTING_LIVES)
                    show_hint_dialog = False  # Reset hint dialog
                    
                    # Log new game start
                    logger.info(f"NEW GAME STARTED! Player '{player.name}' starting level 1 with {STARTING_LIVES} lives")
                    
                    game_state = "briefing" # Transition to briefing screen
                
                # --- NEW: Briefing State Logic ---
                elif game_state == "briefing":
                    if start_mission_button.collidepoint(event.pos):
                        setup_level(current_level) # Setup moles for the level after briefing
                        start_new_round(current_level)
                        show_hint_dialog = False  # Ensure hint dialog is closed
                        
                        # Log mission start
                        logger.info(f"MISSION STARTED! Level {current_level.n_level + 1} ({current_level.theme_name}) - Target: '{current_level.target_data['name']}'")
                        
                        game_state = "playing" # Start playing

                elif game_state == "playing":
                    # Check for hint dialog close
                    if show_hint_dialog:
                        show_hint_dialog = False  # Close dialog on any click
                    # Check for hint button click
                    elif hint_button.collidepoint(event.pos):
                        if player.use_hint():  # Returns True if hint was successfully used
                            show_hint_dialog = True
                            
                            # Log hint usage
                            logger.info(f"HINT USED! Player used hint in level {current_level.n_level + 1}. Hints remaining: {player.hints_remaining}")
                    # --- UPDATED: Hitman Logic for clicks ---
                    # Check if the click was within the active mole's bounding box
                    elif active_mole and active_mole.rect.collidepoint(event.pos):
                        if active_mole.mole_type == 'target':
                            player.total_score += 1
                            current_level.increment_hits()
                            
                            # Log target hit and score earned
                            logger.info(f"TARGET HIT! Player hit target mole '{current_level.target_data['name']}' in level {current_level.n_level + 1}")
                            logger.info(f"SCORE EARNED! Player scored 1 point. Total score: {player.total_score}")
                            
                            if current_level.is_complete():
                                # Update player's highest completed level record
                                if current_level.n_level > player.max_level_reached:
                                    player.max_level_reached = current_level.n_level

                                # Log level completion
                                logger.info(f"LEVEL PASSED! Player completed level {current_level.n_level + 1} ({current_level.theme_name}) with {current_level.player_hits}/{current_level.required_hits} hits")
                                
                                if current_level.n_level + 1 >= MAX_LEVELS:
                                    game_state = "win" # Game won!
                                    logger.info(f"GAME WON! Player completed all {MAX_LEVELS} levels with final score: {player.total_score}")
                                else:
                                    game_state = "level_complete" # Proceed to next level
                            else:
                                start_new_round(current_level) # Continue current level
                        elif active_mole.mole_type == 'civilian':
                            # Penalty for hitting a civilian!
                            current_level.lose_life()
                            
                            # Log turn/life used
                            logger.info(f"TURN USED! Player hit civilian mole in level {current_level.n_level + 1}. Lives remaining: {current_level.life_points}")
                            
                            if not current_level.has_lives():
                                game_state = "game_over" # No lives left
                                logger.info(f"GAME OVER! Player ran out of lives in level {current_level.n_level + 1}. Final score: {player.total_score}")
                            else:
                                start_new_round(current_level) # Continue current level with fewer lives
                    else: # Player missed the active mole (either hit empty space or wrong mole)
                        current_level.lose_life()
                        
                        # Log turn/life used
                        logger.info(f"TURN USED! Player missed target in level {current_level.n_level + 1}. Lives remaining: {current_level.life_points}")
                        
                        if not current_level.has_lives():
                            game_state = "game_over" # No lives left
                            logger.info(f"GAME OVER! Player ran out of lives in level {current_level.n_level + 1}. Final score: {player.total_score}")
                        else:
                            start_new_round(current_level) # Continue current level with fewer lives
                
                elif game_state == "level_complete":
                    if continue_button.collidepoint(event.pos):
                        next_level_num = current_level.n_level + 1
                        player.last_level_played = next_level_num # Track level reached in this run
                        current_level = Level(n_level=next_level_num, starting_lives=STARTING_LIVES)
                        player.reset_level_hint_status()  # Allow hint usage for new level
                        
                        # Log progressing to next level
                        logger.info(f"NEXT LEVEL! Player proceeding to level {next_level_num + 1} ({current_level.theme_name if current_level.theme_data else 'Unknown'})")
                        
                        game_state = "briefing" # Go to briefing for next mission
                    elif quit_button.collidepoint(event.pos):
                        game_state = "home" # Go back to home screen
                
                elif game_state in ["game_over", "win"]:
                    game_state = "home" # Return to home screen from game over/win

        # --- State-based Drawing ---
        if game_state == "playing":
            # Check for round time limit
            if pygame.time.get_ticks() - round_start_time > round_time_limit:
                start_new_round(current_level) # Mole disappears if not hit in time
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