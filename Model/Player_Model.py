from dataclasses import dataclass

@dataclass
class Player:
    Name: str
    Player_ID: int
    Weight:str
    Height:str
    College: str

    def __init__(self, Name: str,Player_ID: int, Weight: str, Height: str, College: str):   
        
        self.Name = Name
        self.Player_ID = Player_ID
        self.Weight = Weight
        self.Height = Height
        self.College = College