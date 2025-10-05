# game/level.py
from game.missions import LEVEL_THEMES

class Level:
    def __init__(self, n_level: int, starting_lives: int):
        self.n_level = n_level
        self.life_points = starting_lives
        
        if 0 <= self.n_level <= 3:
            self.holes = 3
            self.required_hits = 3
        else:
            self.holes = 5
            self.required_hits = 6
        
        self.player_hits = 0
        
        # Load theme data for this level
        self.theme_data = LEVEL_THEMES.get(self.n_level)
        if self.theme_data:
            self.target_data = self.theme_data["target"]
            self.civilian_images = self.theme_data["civilian_images"]
            self.background_image = self.theme_data["background_image"]
            self.theme_name = self.theme_data["name"]
        else:
            # Fallback for missing levels
            print(f"Warning: No theme data for level {self.n_level}")
            self.target_data = None
            self.civilian_images = []
            self.background_image = None
            self.theme_name = f"Level {self.n_level + 1}"

    def increment_hits(self):
        self.player_hits += 1

    def is_complete(self) -> bool:
        return self.player_hits >= self.required_hits

    def lose_life(self):
        self.life_points -= 1

    def has_lives(self) -> bool:
        return self.life_points > 0