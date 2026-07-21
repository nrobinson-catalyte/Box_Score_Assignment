from dataclasses import dataclass

@dataclass
class Team:
    Name: str
    Team_ID: int
    City: str
    State: str
    Arena: str

    def __init__(self, Name: str, Team_ID: int, City: str, State: str, Arena: str):   
        
        self.Name = Name
        self.Team_ID = Team_ID
        self.City = City
        self.State = State
        self.Arena = Arena