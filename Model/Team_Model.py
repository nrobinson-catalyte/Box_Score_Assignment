from dataclasses import dataclass

@dataclass
class Team:
    Name: str
    City: str
    State: str
    Arena: str

    def __init__(self, Name: str, City: str, State: str, Arena: str):   
        
        self.Name = Name
        self.City = City
        self.State = State
        self.Arena = Arena