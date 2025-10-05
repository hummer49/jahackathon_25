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
    
    title_rect = title_text.get_rect(center=(settings.width / 2, settings.height / 2 - 80))
    theme_rect = theme_text.get_rect(center=(settings.width / 2, settings.height / 2 - 20))
    
    display.blit(title_text, title_rect)
    display.blit(theme_text, theme_rect)

    # Draw Start button
    mouse_pos = pygame.mouse.get_pos()
    btn_color = settings.BRIGHT_GREEN if start_button.collidepoint(mouse_pos) else settings.GREEN
    pygame.draw.rect(display, btn_color, start_button)
    start_text = settings.font_medium.render("START", True, settings.WHITE)
    start_text_rect = start_text.get_rect(center=start_button.center)
    display.blit(start_text, start_text_rect)

def draw_game_screen(display, settings, moles, player, level, hint_button=None, show_hint_dialog=False):
    # Draw background instead of solid color
    if hasattr(level, 'background_surface') and level.background_surface:
        display.blit(level.background_surface, (0, 0))
    else:
        display.fill(settings.BLUE)  # Fallback
    
    # # Draw the black "holes" as a background
    # for mole in moles:
    #     pygame.draw.circle(display, settings.BLACK, (mole.x, mole.y), mole.radius)
    
    # Call each mole's own draw method to blit its image
    for mole in moles:
        mole.draw()
    
    # UI Text (Score, Lives, etc.)
    score_text = settings.font_small.render(f"Score: {player.total_score}", True, settings.WHITE)
    lives_text = settings.font_small.render(f"Lives: {level.life_points}", True, settings.WHITE)
    level_text = settings.font_small.render(f"Level: {level.n_level + 1}", True, settings.WHITE)
    hits_text = settings.font_small.render(f"Hits: {level.player_hits} / {level.required_hits}", True, settings.WHITE)
    hints_text = settings.font_small.render(f"Hints: {player.hints_remaining}", True, settings.WHITE)

    display.blit(score_text, (10, 10))
    display.blit(lives_text, (settings.width - 120, 10))
    display.blit(level_text, (10, 50))
    display.blit(hits_text, (settings.width - 170, 50))
    display.blit(hints_text, (10, 90))
    
    # Draw hint button if provided
    if hint_button:
        mouse_pos = pygame.mouse.get_pos()
        # Button is disabled if no hints remaining or already used this level
        button_disabled = player.hints_remaining <= 0 or player.hint_used_this_level
        
        if button_disabled:
            btn_color = settings.BLACK  # Disabled color
        else:
            btn_color = settings.BRIGHT_GREEN if hint_button.collidepoint(mouse_pos) else settings.GREEN
        
        pygame.draw.rect(display, btn_color, hint_button)
        hint_btn_text = settings.font_small.render("HINT", True, settings.WHITE)
        hint_btn_rect = hint_btn_text.get_rect(center=hint_button.center)
        display.blit(hint_btn_text, hint_btn_rect)
    
    # Draw hint dialog if requested
    if show_hint_dialog and level.target_data:
        draw_hint_dialog(display, settings, level.target_data['hint'])

def draw_hint_dialog(display, settings, hint_text):
    """Draw a hint dialog box in the center of the screen."""
    # Dialog box dimensions
    dialog_width = 500
    dialog_height = 150
    dialog_x = (settings.width - dialog_width) // 2
    dialog_y = (settings.height - dialog_height) // 2
    
    # Draw dialog background
    dialog_rect = pygame.Rect(dialog_x, dialog_y, dialog_width, dialog_height)
    pygame.draw.rect(display, settings.BLACK, dialog_rect)
    pygame.draw.rect(display, settings.WHITE, dialog_rect, 3)  # White border
    
    # Draw hint text
    hint_title = settings.font_medium.render("HINT", True, settings.WHITE)
    hint_content = settings.font_small.render(hint_text, True, settings.WHITE)
    close_text = settings.font_small.render("Click anywhere to close", True, settings.WHITE)
    
    title_rect = hint_title.get_rect(center=(settings.width // 2, dialog_y + 30))
    content_rect = hint_content.get_rect(center=(settings.width // 2, dialog_y + 70))
    close_rect = close_text.get_rect(center=(settings.width // 2, dialog_y + 110))
    
    display.blit(hint_title, title_rect)
    display.blit(hint_content, content_rect)
    display.blit(close_text, close_rect)

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