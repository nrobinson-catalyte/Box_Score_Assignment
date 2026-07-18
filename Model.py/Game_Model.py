from dataclasses import dataclass
from datetime import date

@dataclass
class Game:
    Game_ID: int
    Home_Team: str
    Away_Team: str
    Date: date
    Arena: str

    def __init__(self, Game_ID:int, Home_Team: str, Away_Team: str, Date: date, Arena: str):   
        
        self.Game_ID = Game_ID
        self.Home_Team = Home_Team
        self.Away_Team = Away_Team
        self.Date = Date
        self.Arena = Arena