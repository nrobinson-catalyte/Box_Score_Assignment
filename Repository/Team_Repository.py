from Model.Team_Model import Team

class Team_Repository:
    def __init__(self):
        self.teams = []

# Search Team
    def search_team(self, team_name: str):
        for team in self.teams:
            if team.Name == team_name: 
                return team
        return None
# Search Team Stats
    def search_team_stats(self, team_name: str):
        team = self.get_team(team_name)
        if team:
            return {
                "Name": team.Name,
                "City": team.City,
                "State": team.State,
                "Arena": team.Arena
            }

        return None

# Add Team
    def add_team(self, team: Team):
        self.teams.append(team)
# Delete Team
    def delete_team(self, team_name: str):
        for team in self.teams:
            if team.Name == team_name:
                self.teams.remove(team)
                return True
        
        return False  