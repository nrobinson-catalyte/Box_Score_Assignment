from datetime import date
from Model.Game_Model import Game
from Repository.Game_Repository import Game_Repository

class Game_Service:

    def __init__(self, game_repository: Game_Repository):
        self.game_repository = game_repository

    # Get All Games
    def get_all_games(self):
        return self.game_repository.get_all_games()
    # Search Game
    def search_game(self, game_identifier):
        game = self.game_repository.get_game(game_identifier)

        if game is None:
            raise ValueError("Game not found.")

        return game

    # Add Game
    def add_game(self, game: Game):

        # Check for duplicate Game ID
        if self.game_repository.get_game(game.Game_ID):
            raise ValueError("Game ID already exists.")

        # Prevent games in the past
        if game.Date < date.today():
            raise ValueError("Cannot add a game that has already been played.")

        self.game_repository.add_game(game)

        return True

    # Delete Game
    def delete_game(self, game_id: int):

        deleted = self.game_repository.delete_game(game_id)

        if not deleted:
            raise ValueError("Game not found.")

        return True