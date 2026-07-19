from dataclasses import dataclass
from datetime import date

@dataclass
class Game_Stats:
    Game_ID: int # Retrieved From Game_Model
    Points: int
    Assists: int
    Rebounds: int

    def __init__(self, Game_ID: int, Points: int, Assists: int, Rebounds: int):   
        
        self.Game_ID = Game_ID # Retrieved From Game_Model
        self.Points = Points
        self.Assists = Assists
        self.Rebounds = Rebounds
    