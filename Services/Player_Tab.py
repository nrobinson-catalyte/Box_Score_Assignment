from Model.Player_Model import Player
from Repository.Player_Repository import Player_Repository


class Player_Service:

    def __init__(self, player_repository: Player_Repository):
        self.player_repository = player_repository

    # Search Player
    def search_player(self, player_identifier):

        player = self.player_repository.get_player(player_identifier)

        if player is None:
            raise ValueError("Player not found.")

        return player

    # Add Player
    def add_player(self, player: Player):

        # Prevent duplicate Player IDs
        if self.player_repository.get_player(player.Player_ID):
            raise ValueError("Player ID already exists.")

        self.player_repository.add_player(player)

        return True

    # Delete Player
    def delete_player(self, player_identifier):

        deleted = self.player_repository.delete_player(player_identifier)

        if not deleted:
            raise ValueError("Player not found.")

        # Remove associated statistics
        self.player_repository.delete_player_stats(player_identifier)

        return True