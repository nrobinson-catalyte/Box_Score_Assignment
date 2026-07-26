from Repository.Player_Repository import Player_Repository
from Repository.Player_Game_Stats_Repository import Player_Game_Stats_Repository

class Player_Stats_Service:

    def __init__(
        self,
        player_repository: Player_Repository,
        player_game_stats_repository: Player_Game_Stats_Repository
    ):

        self.player_repository = player_repository
        self.player_game_stats_repository = player_game_stats_repository

    # Search Player Stats
    def search_player_stats(self, player_identifier):
        player = self.player_repository.get_player(player_identifier)

        if player is None:
            raise ValueError("Player not found.")

        game_stats = self.player_game_stats_repository.get_player_game_stats(
            player.Player_ID
        )

        if len(game_stats) == 0:
            raise ValueError("No player statistics found.")

        total_points = 0
        total_assists = 0
        total_rebounds = 0

        for stats in game_stats:

            total_points += stats.Points
            total_assists += stats.Assists
            total_rebounds += stats.Rebounds

        games_played = len(game_stats)

        return {
            "Name": player.Name,
            "College": player.College,
            "Points Average": total_points / games_played,
            "Assist Average": total_assists / games_played,
            "Rebound Average": total_rebounds / games_played
        }