from Repository.Team_Repository import Team_Repository

class Team_Stats_Service:
    def __init__(self, team_repository: Team_Repository):

        self.team_repository = team_repository

    # Search Team Stats
    def search_team_stats(self, team_identifier):
        team_stats = self.team_repository.search_team_stats(
            team_identifier
        )
        if team_stats is None:

            raise ValueError("Team not found.")
        return team_stats