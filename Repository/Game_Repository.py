from Model.Game_Model import Game
from Model.Game_Stats import Game_Stats


class Game_Repository:

    def __init__(self):
        self.games = []
        self.game_stats = []
# Search Game
    def get_game(self, game_id: int):
        for game in self.games:
            if game.Game_ID == game_id:
                return game
            
        return None
# Search Game stats
    def add_game_stats(self, stats: Game_Stats):
        self.game_stats.append(stats)

    def get_game_stats(self, game_id: int):
        stats_for_game = []

        for stats in self.game_stats:
            if stats.Game_ID == game_id:
                stats_for_game.append(stats)

        return stats_for_game
# Add Game
    def add_game(self, game: Game):
        self.games.append(game)
# Delete Game
    def delete_game(self, game_id: int):
        for game in self.games:
            if game.Game_ID == game_id:
                self.games.remove(game)

                self.game_stats = [
                    stats for stats in self.game_stats
                    if stats.Game_ID != game_id
                ]

                return True

        return False
