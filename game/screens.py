# # game/screens.py
# import pygame

# def draw_home_screen(display, settings):
#     display.fill(settings.BLACK)
#     title_text = settings.font_large.render("HIT-A-MOLE", True, settings.WHITE)
#     prompt_text = settings.font_small.render("Click anywhere to start", True, settings.WHITE)
#     title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 50))
#     prompt_rect = prompt_text.get_rect(center=(settings.width / 2, settings.height / 2 + 20))
#     display.blit(title_text, title_rect)
#     display.blit(prompt_text, prompt_rect)

# def draw_game_screen(display, settings, moles, player, level):
#     display.fill(settings.BLUE)
#     for mole in moles:
#         mole.draw(red=settings.BRIGHT_RED, black=settings.BLACK)
    
#     score_text = settings.font_small.render(f"Score: {player.total_score}", True, settings.WHITE)
#     lives_text = settings.font_small.render(f"Lives: {level.life_points}", True, settings.WHITE)
#     level_text = settings.font_small.render(f"Level: {level.n_level + 1}", True, settings.WHITE)
#     hits_text = settings.font_small.render(f"Hits: {level.player_hits} / {level.required_hits}", True, settings.WHITE)

#     display.blit(score_text, (10, 10))
#     display.blit(lives_text, (settings.width - 120, 10))
#     display.blit(level_text, (10, 50))
#     display.blit(hits_text, (settings.width - 170, 50))

# def draw_level_complete_screen(display, settings, player, continue_btn, quit_btn):
#     display.fill(settings.BLACK)
    
#     title_text = settings.font_large.render(f"Level {player.last_level_played + 1} Completed!", True, settings.WHITE)
#     # sub_title_text = settings.font_large.render("Level Completed!", True, settings.WHITE)
#     score_text = settings.font_small.render(f"Current Score: {player.total_score}", True, settings.WHITE)
#     title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 80))
#     score_rect = score_text.get_rect(center=(settings.width / 2, settings.height / 2 - 20))
#     display.blit(title_text, title_rect)
#     display.blit(score_text, score_rect)

#     mouse_pos = pygame.mouse.get_pos()
    
#     continue_color = settings.BRIGHT_GREEN if continue_btn.collidepoint(mouse_pos) else settings.GREEN
#     pygame.draw.rect(display, continue_color, continue_btn)
#     continue_text = settings.font_medium.render("CONTINUE", True, settings.WHITE)
#     continue_text_rect = continue_text.get_rect(center=continue_btn.center)
#     display.blit(continue_text, continue_text_rect)

#     quit_color = settings.BRIGHT_RED if quit_btn.collidepoint(mouse_pos) else settings.RED
#     pygame.draw.rect(display, quit_color, quit_btn)
#     quit_text = settings.font_medium.render("QUIT", True, settings.WHITE)
#     quit_text_rect = quit_text.get_rect(center=quit_btn.center)
#     display.blit(quit_text, quit_text_rect)

# # def draw_game_over_screen(display, settings, player):
# #     display.fill(settings.BLACK)
# #     title_text = settings.font_large.render("GAME OVER", True, settings.BRIGHT_RED)
# #     score_text = settings.font_small.render(f"Final Score: {player.total_score}", True, settings.WHITE)
# #     prompt_text = settings.font_small.render("Click to return to menu", True, settings.WHITE)
# #     title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 50))
# #     score_rect = score_text.get_rect(center=(settings.width / 2, settings.height / 2 + 20))
# #     prompt_rect = prompt_text.get_rect(center=(settings.width / 2, settings.height / 2 + 60))
# #     display.blit(title_text, title_rect); display.blit(score_text, score_rect); display.blit(prompt_text, prompt_rect)

# def draw_game_over_screen(display, settings, player):
#     display.fill(settings.BLACK)
#     title_text = settings.font_large.render("GAME OVER", True, settings.BRIGHT_RED)
#     score_text = settings.font_small.render(f"Final Score: {player.total_score}", True, settings.WHITE)
    
#     # Add text to show what level they were on
#     level_text = settings.font_small.render(f"You reached Level: {player.last_level_played + 1}", True, settings.WHITE)
    
#     prompt_text = settings.font_small.render("Click to return to menu", True, settings.WHITE)
    
#     # Positioning and blitting
#     title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 80))
#     score_rect = score_text.get_rect(center=(settings.width / 2, settings.height / 2 - 20))
#     level_rect = level_text.get_rect(center=(settings.width / 2, settings.height / 2 + 20))
#     prompt_rect = prompt_text.get_rect(center=(settings.width / 2, settings.height / 2 + 70))
    
#     display.blit(title_text, title_rect)
#     display.blit(score_text, score_rect)
#     display.blit(level_text, level_rect)
#     display.blit(prompt_text, prompt_rect)

# def draw_win_screen(display, settings, player):
#     display.fill(settings.BLACK)
#     title_text = settings.font_large.render("YOU WIN!", True, settings.BRIGHT_GREEN)
#     score_text = settings.font_small.render(f"Final Score: {player.total_score}", True, settings.WHITE)
#     prompt_text = settings.font_small.render("Click to return to menu", True, settings.WHITE)
#     title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 50))
#     score_rect = score_text.get_rect(center=(settings.width / 2, settings.height / 2 + 20))
#     prompt_rect = prompt_text.get_rect(center=(settings.width / 2, settings.height / 2 + 60))
#     display.blit(title_text, title_rect); display.blit(score_text, score_rect); display.blit(prompt_text, prompt_rect)

import pygame

def draw_home_screen(display, settings, player):
    display.fill(settings.BLACK)
    title_text = settings.font_large.render("HIT-A-MOLE", True, settings.WHITE)
    prompt_text = settings.font_small.render("Click anywhere to start", True, settings.WHITE)
    
    # Display the highest level the player has completed
    completed_level_display = player.max_level_reached + 1
    max_level_text = settings.font_small.render(f"Highest Level Completed: {completed_level_display}", True, settings.WHITE)

    title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 80))
    prompt_rect = prompt_text.get_rect(center=(settings.width / 2, settings.height / 2 - 20))
    max_level_rect = max_level_text.get_rect(center=(settings.width / 2, settings.height / 2 + 20))
    
    display.blit(title_text, title_rect)
    display.blit(prompt_text, prompt_rect)
    display.blit(max_level_text, max_level_rect)

def draw_briefing_screen(display, settings, level, start_button):
    display.fill(settings.BLACK)
    
    title_text = settings.font_large.render(f"Mission {level.n_level + 1}", True, settings.WHITE)
    theme_text = settings.font_medium.render(f"Location: {level.theme_name}", True, settings.WHITE)
    target_text = settings.font_medium.render(f"Target: {level.target_data['name']}", True, settings.WHITE)
    hint_text = settings.font_small.render(f"Hint: {level.target_data['hint']}", True, settings.WHITE)
    
    title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 140))
    theme_rect = theme_text.get_rect(center=(settings.width / 2, settings.height / 2 - 90))
    target_rect = target_text.get_rect(center=(settings.width / 2, settings.height / 2 - 50))
    hint_rect = hint_text.get_rect(center=(settings.width / 2, settings.height / 2))
    
    display.blit(title_text, title_rect)
    display.blit(theme_text, theme_rect)
    display.blit(target_text, target_rect)
    display.blit(hint_text, hint_rect)

    # Draw Start button
    mouse_pos = pygame.mouse.get_pos()
    btn_color = settings.BRIGHT_GREEN if start_button.collidepoint(mouse_pos) else settings.GREEN
    pygame.draw.rect(display, btn_color, start_button)
    start_text = settings.font_medium.render("START", True, settings.WHITE)
    start_text_rect = start_text.get_rect(center=start_button.center)
    display.blit(start_text, start_text_rect)

def draw_game_screen(display, settings, moles, player, level):
    # Draw background instead of solid color
    if hasattr(level, 'background_surface') and level.background_surface:
        display.blit(level.background_surface, (0, 0))
    else:
        display.fill(settings.BLUE)  # Fallback
    
    # Draw the black "holes" as a background
    for mole in moles:
        pygame.draw.circle(display, settings.BLACK, (mole.x, mole.y), mole.radius)
    
    # Call each mole's own draw method to blit its image
    for mole in moles:
        mole.draw()
    
    # UI Text (Score, Lives, etc.)
    score_text = settings.font_small.render(f"Score: {player.total_score}", True, settings.WHITE)
    lives_text = settings.font_small.render(f"Lives: {level.life_points}", True, settings.WHITE)
    level_text = settings.font_small.render(f"Level: {level.n_level + 1}", True, settings.WHITE)
    hits_text = settings.font_small.render(f"Hits: {level.player_hits} / {level.required_hits}", True, settings.WHITE)

    display.blit(score_text, (10, 10))
    display.blit(lives_text, (settings.width - 120, 10))
    display.blit(level_text, (10, 50))
    display.blit(hits_text, (settings.width - 170, 50))

def draw_level_complete_screen(display, settings, player, level, continue_btn, quit_btn):
    display.fill(settings.BLACK)
    
    title_text = settings.font_large.render(f"Mission {level.n_level + 1} Complete!", True, settings.WHITE)
    score_text = settings.font_small.render(f"Current Score: {player.total_score}", True, settings.WHITE)
    
    title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 80))
    score_rect = score_text.get_rect(center=(settings.width / 2, settings.height / 2 - 20))
    
    display.blit(title_text, title_rect)
    display.blit(score_text, score_rect)

    # Button drawing logic
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

def draw_game_over_screen(display, settings, player):
    display.fill(settings.BLACK)
    title_text = settings.font_large.render("GAME OVER", True, settings.BRIGHT_RED)
    score_text = settings.font_small.render(f"Final Score: {player.total_score}", True, settings.WHITE)
    level_text = settings.font_small.render(f"You reached Level: {player.last_level_played + 1}", True, settings.WHITE)
    prompt_text = settings.font_small.render("Click to return to menu", True, settings.WHITE)
    
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
    
    display.blit(title_text, title_rect)
    display.blit(score_text, score_rect)
    display.blit(prompt_text, prompt_rect)