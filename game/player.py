# game/player.py
class Player:
    def __init__(self, name: str = "Agent 48"):
        self.name = name
        self.total_score = 0
    
    def reset(self):
        self.total_score = 0