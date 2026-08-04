from Model.Team_Model import Team
from Repository.Team_Repository import Team_Repository


class Team_Service:

    def __init__(self, team_repository: Team_Repository):
        self.team_repository = team_repository

    # Get All Teams
    def get_all_teams(self):
        return self.team_repository.get_all_teams()
    
    # Search Team
    def search_team(self, team_identifier):

        team = self.team_repository.search_team(team_identifier)

        if team is None:
            raise ValueError("Team not found.")

        return team

    # Add Team
    def add_team(self, team: Team):

        # Check for duplicate team
        if self.team_repository.search_team(team.Name):
            raise ValueError("Team already exists.")

        self.team_repository.add_team(team)

        return True


    # Delete Team
    def delete_team(self, team_identifier):

        deleted = self.team_repository.delete_team(team_identifier)

        if not deleted:
            raise ValueError("Team not found.")

        return True