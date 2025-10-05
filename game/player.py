class Player:
    def __init__(self, name: str = "Agent 48"):
        self.name = name
        self.total_score = 0
        self.max_level_reached = -1
        # Add the new variable for the current game session
        self.last_level_played = 0
        # Hint system tracking
        self.hints_remaining = 3
        self.hint_used_this_level = False
    
    def reset(self):
        """Resets stats for a new game run."""
        self.total_score = 0
        # Reset the last level played for the new game
        self.last_level_played = 0
        # Reset hint system for new game
        self.hints_remaining = 3
        self.hint_used_this_level = False
    
    def use_hint(self):
        """Uses a hint if available. Returns True if hint was used, False otherwise."""
        if self.hints_remaining > 0 and not self.hint_used_this_level:
            self.hints_remaining -= 1
            self.hint_used_this_level = True
            return True
        return False
    
    def reset_level_hint_status(self):
        """Resets hint usage for the current level (call when starting new level)."""
        self.hint_used_this_level = False