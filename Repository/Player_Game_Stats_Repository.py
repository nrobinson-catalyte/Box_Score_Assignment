from Model.Player_Game_Stats_Model import Player_Game_Stats


class Player_Game_Stats_Repository:

    def __init__(self):
        self.player_game_stats = []


    # Add Player Game Stats
    def add_player_game_stats(self, stats: Player_Game_Stats):

        self.player_game_stats.append(stats)


    # Search Player Game Stats
    def get_player_game_stats(self, player_identifier):

        stats_for_player = []

        for stats in self.player_game_stats:

            if (
                stats.Player_ID == player_identifier or
                stats.Name == player_identifier
            ):
                stats_for_player.append(stats)

        return stats_for_player