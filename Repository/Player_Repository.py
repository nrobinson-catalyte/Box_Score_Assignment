from Model.Player_Model import Player
from Database.database import get_connection


class Player_Repository:

    # ============================================================
    # Search Player
    # ============================================================
    def get_player(self, player_identifier):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Players
            WHERE Player_ID = ?
               OR Name = ?
            """,
            (player_identifier, player_identifier)
        )

        row = cursor.fetchone()

        connection.close()

        if row is None:
            return None

        return Player(
            Player_ID=row[0],
            Name=row[1],
            Height=row[2],
            Weight=row[3],
            College=row[4]
        )

    # ============================================================
    # Add Player
    # ============================================================
    def add_player(self, player):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO Players
            (Player_ID, Name, Height, Weight, College)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                player.Player_ID,
                player.Name,
                player.Height,
                player.Weight,
                player.College,
            ),
        )

        connection.commit()
        connection.close()

    # ============================================================
    # Get All Players
    # ============================================================
    def get_all_players(self):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Players
            ORDER BY Name
            """
        )

        rows = cursor.fetchall()

        connection.close()

        players = []

        for row in rows:
            players.append(
                Player(
                    Player_ID=row[0],
                    Name=row[1],
                    Height=row[2],
                    Weight=row[3],
                    College=row[4],
                )
            )

        return players

    # ============================================================
    # Get Players Map
    # ============================================================
    def get_players_map(self):

        players = self.get_all_players()

        return {
            player.Player_ID: player.Name
            for player in players
        }

    # ============================================================
    # Update Player
    # ============================================================
    def update_player(
        self,
        player_identifier,
        new_name=None,
        weight=None,
        height=None,
        college=None,
    ):

        player = self.get_player(player_identifier)

        if player is None:
            return False

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE Players
            SET Name = ?,
                Weight = ?,
                Height = ?,
                College = ?
            WHERE Player_ID = ?
            """,
            (
                new_name if new_name is not None else player.Name,
                weight if weight is not None else player.Weight,
                height if height is not None else player.Height,
                college if college is not None else player.College,
                player.Player_ID,
            ),
        )

        connection.commit()
        connection.close()

        return True

    # ============================================================
    # Delete Player
    # ============================================================
    def delete_player(self, player_identifier):

        player = self.get_player(player_identifier)

        if player is None:
            return False

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM Players
            WHERE Player_ID = ?
            """,
            (player.Player_ID,),
        )

        connection.commit()
        connection.close()

        return True