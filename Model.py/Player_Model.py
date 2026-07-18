from dataclasses import dataclass

@dataclass
class Player:
    Name: str
    Weight:str
    Height:str
    College: str

    def __init__(self, Name:str, Weight: str, Height: str, College: str):   
        
        self.Name = Name
        self.Weight = Weight
        self.Height = Height
        self.College = College