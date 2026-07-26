from Model.Team_Model import Team

class Team_Repository:
    def __init__(self):
        self.teams = []

# Search Team
    def search_team(self, team_identifier):

        for team in self.teams:
            if (
                team.Name == team_identifier or
                team.City == team_identifier or
                team.State == team_identifier or
                team.Arena == team_identifier or
                team.Team_ID == team_identifier
            ):
                return team
        return None
# Search Team Stats
def search_team_stats(self, team_identifier):
    team = self.search_team(team_identifier)
    if team:
        return {
            "Team": team.Name,
            "Location": f"{team.City}, {team.State}",
            "Record": team.Record
        }

    return None

# Add Team
    def add_team(self, team: Team):
        self.teams.append(team)

# Update Team
    def update_team(self, team_name: str, city=None, state=None, arena=None, new_name=None):
        team = self.search_team(team_name)

        if team is None:
            return False

        if new_name is not None:
            team.Name = new_name
        if city is not None:
            team.City = city
        if state is not None:
            team.State = state
        if arena is not None:
            team.Arena = arena

        return True
# Record of Team
        # Add Team Win
    def add_win(self, team_identifier):

        team = self.search_team(team_identifier)
        if team is None:
            return False
        wins, losses = team.Record.split("-")
        wins = int(wins)
        losses = int(losses)
        wins += 1
        team.Record = f"{wins}-{losses}"

        return True   
        # Add Team Loss
    def add_loss(self, team_identifier):
        team = self.search_team(team_identifier)

        if team is None:
            return False
        wins, losses = team.Record.split("-")
        wins = int(wins)
        losses = int(losses)
        losses += 1
        team.Record = f"{wins}-{losses}"

        return True 
    # Delete Team
    def delete_team(self, team_identifier):

        for team in self.teams:
            if (
                team.Team_ID == team_identifier or
                team.Name == team_identifier or
                team.City == team_identifier or
                team.State == team_identifier or
                team.Arena == team_identifier
            ):
                self.teams.remove(team)
                return True

        return False