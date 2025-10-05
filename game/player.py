class Player:
    def __init__(self, name: str = "Agent 48"):
        self.name = name
        self.total_score = 0
        self.max_level_reached = -1
        # Add the new variable for the current game session
        self.last_level_played = 0
    
    def reset(self):
        """Resets stats for a new game run."""
        self.total_score = 0
        # Reset the last level played for the new game
        self.last_level_played = 0