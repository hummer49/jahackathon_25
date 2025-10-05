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

def main():
    pygame.init()
    settings = Settings()
    player = Player()
    display = pygame.display.set_mode(size=(settings.width, settings.height))
    pygame.display.set_caption(settings.title)

    STARTING_LIVES = 3
    MAX_LEVELS = 7 # Last level is index 6
    
    current_level, moles, active_mole = None, [], None
    round_time_limit, round_start_time = 1000, 0
    game_state = "home"

    button_w, button_h = 200, 70
    button_y = settings.height / 2 + 80
    continue_button = pygame.Rect(settings.width/4 - button_w/2, button_y, button_w, button_h)
    quit_button = pygame.Rect(settings.width*3/4 - button_w/2, button_y, button_w, button_h)

    def setup_level(level_obj):
        nonlocal moles
        moles.clear()
        for i in range(level_obj.holes):
            x = (i + 1) * (settings.width // (level_obj.holes + 1))
            moles.append(Mole(x, settings.height / 2, display))

    def start_new_round():
        nonlocal active_mole, round_start_time
        if active_mole: active_mole.is_active = False
        if moles: active_mole = random.choice(moles); active_mole.is_active = True
        round_start_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "home":
                    player.reset()
                    current_level = Level(n_level=0, starting_lives=STARTING_LIVES)
                    setup_level(current_level)
                    start_new_round()
                    game_state = "playing"
                
                elif game_state == "playing":
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    dist = ((mouse_x - active_mole.x)**2 + (mouse_y - active_mole.y)**2)**0.5

                    if dist <= active_mole.radius:
                        player.total_score += 1
                        current_level.increment_hits()
                        
                        if current_level.is_complete():
                            if current_level.n_level + 1 >= MAX_LEVELS:
                                game_state = "win"
                            else:
                                game_state = "level_complete"
                        else:
                            start_new_round()
                    else:
                        current_level.lose_life()
                        if not current_level.has_lives():
                            game_state = "game_over"
                        else:
                            start_new_round()
                
                elif game_state == "level_complete":
                    mouse_pos = event.pos
                    if continue_button.collidepoint(mouse_pos):
                        next_level_num = current_level.n_level + 1
                        current_level = Level(n_level=next_level_num, starting_lives=STARTING_LIVES)
                        setup_level(current_level)
                        start_new_round()
                        game_state = "playing"
                    elif quit_button.collidepoint(mouse_pos):
                        game_state = "home"
                
                elif game_state in ["game_over", "win"]:
                    game_state = "home"

        if game_state == "playing":
            if pygame.time.get_ticks() - round_start_time > round_time_limit:
                start_new_round()
            screens.draw_game_screen(display, settings, moles, player, current_level)
        
        elif game_state == "home":
            screens.draw_home_screen(display, settings)
        
        elif game_state == "level_complete":
            screens.draw_level_complete_screen(display, settings, player, continue_button, quit_button)

        elif game_state == "game_over":
            screens.draw_game_over_screen(display, settings, player)
            
        elif game_state == "win":
            screens.draw_win_screen(display, settings, player)

        pygame.display.flip()
        settings.clock.tick(60)

if __name__ == "__main__":
    main()