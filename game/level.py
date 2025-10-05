# game/level.py
from game.missions import TARGETS, CIVILIAN_MOLES
import random
class Level:
    def __init__(self, n_level: int, starting_lives: int):
        self.n_level = n_level
        self.life_points = starting_lives
        
        if 0 <= self.n_level < 2:
            self.holes = 4
            self.required_hits = 3
            self.mole_duration = 1500
        elif self.n_level < 4:
            self.holes = 6
            self.required_hits = 6
            self.mole_duration = 1000
        else:
            self.holes = 9
            self.required_hits = 8
            self.mole_duration = 500
        
        self.player_hits = 0
        # Load the target for this level
        self.target_data = TARGETS.get(self.n_level)

        # Get a list of civilian mole images for this level, excluding the target's image
        self.civilian_images = [img for img in CIVILIAN_MOLES if img != self.target_data["image_path"]]


    def increment_hits(self):
        self.player_hits += 1

    def is_complete(self) -> bool:
        return self.player_hits >= self.required_hits

    def lose_life(self):
        self.life_points -= 1

    def has_lives(self) -> bool:
        return self.life_points > 0