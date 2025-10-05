# game/screens.py
import pygame

def draw_home_screen(display, settings):
    display.fill(settings.BLACK)
    title_text = settings.font_large.render("HIT-A-MOLE", True, settings.WHITE)
    prompt_text = settings.font_small.render("Click anywhere to start", True, settings.WHITE)
    title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 50))
    prompt_rect = prompt_text.get_rect(center=(settings.width / 2, settings.height / 2 + 20))
    display.blit(title_text, title_rect)
    display.blit(prompt_text, prompt_rect)

def draw_game_screen(display, settings, moles, player, level):
    display.fill(settings.BLUE)
    for mole in moles:
        mole.draw(red=settings.BRIGHT_RED, black=settings.BLACK)
    
    score_text = settings.font_small.render(f"Score: {player.total_score}", True, settings.WHITE)
    lives_text = settings.font_small.render(f"Lives: {level.life_points}", True, settings.WHITE)
    level_text = settings.font_small.render(f"Level: {level.n_level + 1}", True, settings.WHITE)
    hits_text = settings.font_small.render(f"Hits: {level.player_hits} / {level.required_hits}", True, settings.WHITE)

    display.blit(score_text, (10, 10))
    display.blit(lives_text, (settings.width - 120, 10))
    display.blit(level_text, (10, 50))
    display.blit(hits_text, (settings.width - 170, 50))

def draw_level_complete_screen(display, settings, player, continue_btn, quit_btn):
    display.fill(settings.BLACK)
    
    title_text = settings.font_large.render(f"Level {player.last_level_played + 1} Completed!", True, settings.WHITE)
    # sub_title_text = settings.font_large.render("Level Completed!", True, settings.WHITE)
    score_text = settings.font_small.render(f"Current Score: {player.total_score}", True, settings.WHITE)
    title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 80))
    score_rect = score_text.get_rect(center=(settings.width / 2, settings.height / 2 - 20))
    display.blit(title_text, title_rect)
    display.blit(score_text, score_rect)

    mouse_pos = pygame.mouse.get_pos()
    
    continue_color = settings.BRIGHT_GREEN if continue_btn.collidepoint(mouse_pos) else settings.GREEN
    pygame.draw.rect(display, continue_color, continue_btn)
    continue_text = settings.font_medium.render("CONTINUE", True, settings.WHITE)
    continue_text_rect = continue_text.get_rect(center=continue_btn.center)
    display.blit(continue_text, continue_text_rect)

    quit_color = settings.BRIGHT_RED if quit_btn.collidepoint(mouse_pos) else settings.RED
    pygame.draw.rect(display, quit_color, quit_btn)
    quit_text = settings.font_medium.render("QUIT", True, settings.WHITE)
    quit_text_rect = quit_text.get_rect(center=quit_btn.center)
    display.blit(quit_text, quit_text_rect)

# def draw_game_over_screen(display, settings, player):
#     display.fill(settings.BLACK)
#     title_text = settings.font_large.render("GAME OVER", True, settings.BRIGHT_RED)
#     score_text = settings.font_small.render(f"Final Score: {player.total_score}", True, settings.WHITE)
#     prompt_text = settings.font_small.render("Click to return to menu", True, settings.WHITE)
#     title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 50))
#     score_rect = score_text.get_rect(center=(settings.width / 2, settings.height / 2 + 20))
#     prompt_rect = prompt_text.get_rect(center=(settings.width / 2, settings.height / 2 + 60))
#     display.blit(title_text, title_rect); display.blit(score_text, score_rect); display.blit(prompt_text, prompt_rect)

def draw_game_over_screen(display, settings, player):
    display.fill(settings.BLACK)
    title_text = settings.font_large.render("GAME OVER", True, settings.BRIGHT_RED)
    score_text = settings.font_small.render(f"Final Score: {player.total_score}", True, settings.WHITE)
    
    # Add text to show what level they were on
    level_text = settings.font_small.render(f"You reached Level: {player.last_level_played + 1}", True, settings.WHITE)
    
    prompt_text = settings.font_small.render("Click to return to menu", True, settings.WHITE)
    
    # Positioning and blitting
    title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 80))
    score_rect = score_text.get_rect(center=(settings.width / 2, settings.height / 2 - 20))
    level_rect = level_text.get_rect(center=(settings.width / 2, settings.height / 2 + 20))
    prompt_rect = prompt_text.get_rect(center=(settings.width / 2, settings.height / 2 + 70))
    
    display.blit(title_text, title_rect)
    display.blit(score_text, score_rect)
    display.blit(level_text, level_rect)
    display.blit(prompt_text, prompt_rect)

def draw_win_screen(display, settings, player):
    display.fill(settings.BLACK)
    title_text = settings.font_large.render("YOU WIN!", True, settings.BRIGHT_GREEN)
    score_text = settings.font_small.render(f"Final Score: {player.total_score}", True, settings.WHITE)
    prompt_text = settings.font_small.render("Click to return to menu", True, settings.WHITE)
    title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 50))
    score_rect = score_text.get_rect(center=(settings.width / 2, settings.height / 2 + 20))
    prompt_rect = prompt_text.get_rect(center=(settings.width / 2, settings.height / 2 + 60))
    display.blit(title_text, title_rect); display.blit(score_text, score_rect); display.blit(prompt_text, prompt_rect)