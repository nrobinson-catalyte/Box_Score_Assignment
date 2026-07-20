from dataclasses import dataclass

@dataclass
class Player_Game_Stats:
    Game_ID: int # Retrieved From Game_Model
    Player_ID: int
    Name: str
    Points: int
    Assists: int
    Rebounds: int

    def __init__(self, Game_ID: int, Player_ID: int, Name: str, Points: int, Assists: int, Rebounds: int):   
        
        self.Game_ID = Game_ID # Retrieved From Game_Model
        self.Player_ID = Player_ID
        self.Name = Name
        self.Points = Points
        self.Assists = Assists
        self.Rebounds = Rebounds