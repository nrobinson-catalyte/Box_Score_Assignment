from Model.Player_Model import Player


class Player_Repository:

    def __init__(self):
        self.Players = []
        self.Player_Stats = []
        self.Player_Game_Stats = []
# Search Player
def get_player(self, player_identifier):
    for player in self.players:
        if player.Player_ID == player_identifier or player.Name == player_identifier:
            return player

    return None


# Search Player Stats
def get_player_stats(self, player_identifier):
    for stats in self.player_stats:
        if stats.Player_ID == player_identifier or stats.Name == player_identifier:
            return stats

    return None


# Add Player
def add_player(self, player: Player):
    self.players.append(player)


# Delete Player
def delete_player(self, player_identifier):

    for player in self.players:
        if player.Player_ID == player_identifier or player.Name == player_identifier:
            self.players.remove(player)
            return True

    return False


# Delete Player Stats
def delete_player_stats(self, player_identifier):

    self.player_stats = [
        stats for stats in self.player_stats
        if stats.Player_ID != player_identifier 
        and stats.Name != player_identifier
    ]

    self.player_game_stats = [
        stats for stats in self.player_game_stats
        if stats.Player_ID != player_identifier
    ]

    return True