from dataclasses import dataclass

@dataclass 
class Player_Stats_Model:
    Name: str
    Player_ID: int # Retrieved From Game_Model
    Points_Average: float
    Assist_Average: float
    Rebounds_Average: float

    def __init__(self, Name: str, Player_ID: int, Points_Average: float, Assist_Average: float, Rebounds_Average: float):   
        
        self.Name = Name
        self.Player_ID = Player_ID
        self.Points_Average = Points_Average
        self.Assist_Average = Assist_Average
        self.Rebounds_Average = Rebounds_Average
