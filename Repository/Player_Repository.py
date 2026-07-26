from Model.Player_Model import Player


class Player_Repository:

    def __init__(self):
        self.players
        self.player_stats
        self.player_game_stats
# Search Player
def get_player(self, player_identifier):

    for player in self.players:
        if (
            player.Player_ID == player_identifier or
            player.Name == player_identifier or
            player.Weight == player_identifier or
            player.Height == player_identifier or
            player.College == player_identifier
        ):
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

# Update Player
def update_player(self, player_identifier, new_name=None, weight=None, height=None, college=None):
    player = self.get_player(player_identifier)

    if player is None:
        return False

    if new_name is not None:
        player.Name = new_name
    if weight is not None:
        player.Weight = weight
    if height is not None:
        player.Height = height
    if college is not None:
        player.College = college

    return True

# Delete Player
def delete_player(self, player_identifier):

    for player in self.players:
        if (
            player.Player_ID == player_identifier or
            player.Name == player_identifier or
            player.Weight == player_identifier or
            player.Height == player_identifier or
            player.College == player_identifier
        ):
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