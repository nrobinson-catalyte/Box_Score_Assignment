from __future__ import annotations

import os
from decimal import Decimal, InvalidOperation
from typing import Callable
from datetime import datetime

from Model.Game_Model import Game
from Model.Game_Stats import Game_Stats
from Model.Player_Game_Stats_Model import Player_Game_Stats
from Model.Player_Model import Player
from Model.Player_Stats_Model import Player_Stats
from Model.Team_Model import Team
from Repository.Player_Repository import Player_Repository
from Repository.Game_Repository import Game_Repository
from Repository.Player_Game_Stats_Repository import Player_Game_Stats_Repository
from Repository.Team_Repository import Team_Repository
from Services.Search_Tab.Player_Stats_Service import Player_Stats_Service
from Services.Search_Tab.Team_Stats_Service import Team_Stats_Service
from Services.Game_Tab import Game_Service
from Services.Player_Tab import Player_Service
from Services.Team_Tab import Team_Service

# ============================================================
# TERMINAL COLORS
# ============================================================

class Colors:
    # Reset / Styles
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    REVERSE = "\033[7m"

    # Standard Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright Colors
    BRIGHT_BLACK = "\033[90m"    # Gray
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # Aliases
    GRAY = BRIGHT_BLACK
    GREY = BRIGHT_BLACK

WIDTH = 80


def enable_windows_ansi() -> None:
    """Enable ANSI colors in supported Windows terminals."""
    if os.name == "nt":
        os.system("")


enable_windows_ansi()

# ============================================================
# TERMINAL DISPLAY HELPERS
# ============================================================

def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def colored(text: str, color: str) -> str:
    """Wrap text in an ANSI color code."""
    return f"{color}{text}{Colors.RESET}"


def print_box_title(title: str, subtitle: str | None = None) -> None:
    """Print a centered title inside a Unicode box."""
    print(colored("╔" + "═" * (WIDTH - 2) + "╗", Colors.CYAN))
    print(
        colored(
            "║" + title.center(WIDTH - 2) + "║",
            Colors.CYAN + Colors.BOLD,
        )
    )

    if subtitle:
        print(
            colored(
                "║" + subtitle.center(WIDTH - 2) + "║",
                Colors.CYAN,
            )
        )

    print(colored("╚" + "═" * (WIDTH - 2) + "╝", Colors.CYAN))


def print_section(title: str) -> None:
    """Print a consistent section heading."""
    print()
    print(colored("─" * WIDTH, Colors.BLUE))
    print(colored(title.center(WIDTH), Colors.BLUE + Colors.BOLD))
    print(colored("─" * WIDTH, Colors.BLUE))


def print_success(message: str) -> None:
    """Print a success message."""
    print(colored(f"\n✓ {message}", Colors.GREEN + Colors.BOLD))


def print_error(message: str) -> None:
    """Print an error message."""
    print(colored(f"\n✗ {message}", Colors.RED + Colors.BOLD))


def print_warning(message: str) -> None:
    """Print a warning message."""
    print(colored(f"\n! {message}", Colors.YELLOW + Colors.BOLD))


def print_info(message: str) -> None:
    """Print an informational message."""
    print(colored(f"\nℹ {message}", Colors.CYAN))


def pause() -> None:
    """Pause before returning to the main menu."""
    input(colored("\nPress Enter to return to the main menu...", Colors.DIM))


def read_nonempty(prompt: str) -> str:
    """Read a required text value."""
    while True:
        value = input(colored(prompt, Colors.WHITE)).strip()
        if value:
            return value
        print_warning("This field cannot be blank.")


def read_optional_text(prompt: str) -> str | None:
    """Read optional text and return None when left blank."""
    value = input(colored(prompt, Colors.WHITE)).strip()
    return value or None


def read_float(prompt: str, minimum: float = 0) -> float:
    """Read a numeric value with a minimum."""
    while True:
        raw_value = input(colored(prompt, Colors.WHITE)).strip()

        try:
            value = float(Decimal(raw_value))
        except (InvalidOperation, ValueError):
            print_warning("Please enter a valid number.")
            continue

        if value < minimum:
            print_warning(f"Value must be at least {minimum}.")
            continue

        return value


def read_positive_float(prompt: str) -> float:
    """Read a number greater than zero."""
    while True:
        value = read_float(prompt, minimum=0)
        if value > 0:
            return value
        print_warning("Value must be greater than 0.")


def read_int(prompt: str, minimum: int = 1) -> int:
    """Read a valid integer with a minimum."""
    while True:
        raw_value = input(colored(prompt, Colors.WHITE)).strip()

        try:
            value = int(raw_value)
        except ValueError:
            print_warning("Please enter a whole number.")
            continue

        if value < minimum:
            print_warning(f"Value must be at least {minimum}.")
            continue

        return value


def confirm(prompt: str) -> bool:
    """Ask the user to confirm an action."""
    response = input(
        colored(f"{prompt} Type YES to confirm: ", Colors.YELLOW)
    ).strip()
    return response.upper() == "YES"

# ============================================================
# TABLE DISPLAYS
# ============================================================

def display_players(players: list[Player]) -> None:
    """Display all players in a table format."""

    clear_screen()
    print_box_title("PLAYER LIST")

    print(
        colored(
            f"{'ID':<8}{'NAME':<25}{'HEIGHT':<12}{'WEIGHT':<12}{'COLLEGE':<25}",
            Colors.YELLOW + Colors.BOLD
        )
    )

    print(colored("-" * WIDTH, Colors.BLUE))

    for player in players:
        print(
            f"{player.Player_ID:<8}"
            f"{player.Name:<25}"
            f"{player.Height:<12}"
            f"{player.Weight:<12}"
            f"{player.College:<25}"
        )

    print(colored("-" * WIDTH, Colors.BLUE))

    pause()

def display_teams(teams: list[Team]) -> None:
    """Display all teams in a table format."""

    clear_screen()
    print_box_title("TEAM LIST")

    print(
        colored(
            f"{'ID':<8}{'TEAM':<20}{'CITY':<18}{'STATE':<10}{'ARENA':<25}{'RECORD':<10}",
            Colors.YELLOW + Colors.BOLD
        )
    )

    print(colored("-" * WIDTH, Colors.BLUE))

    for team in teams:
        print(
            f"{team.Team_ID:<8}"
            f"{team.Name:<20}"
            f"{team.City:<18}"
            f"{team.State:<10}"
            f"{team.Arena:<25}"
            f"{team.Record:<10}"
        )

    print(colored("-" * WIDTH, Colors.BLUE))

    pause()

def display_games(games: list[Game]) -> None:
    """Display all games in a table format."""

    clear_screen()
    print_box_title("GAME LIST")

    print(
        colored(
            f"{'ID':<8}{'HOME TEAM':<20}{'AWAY TEAM':<20}{'DATE':<15}{'ARENA':<25}",
            Colors.YELLOW + Colors.BOLD
        )
    )

    print(colored("-" * WIDTH, Colors.BLUE))

    for game in games:
        print(
            f"{game.Game_ID:<8}"
            f"{game.Home_Team:<20}"
            f"{game.Away_Team:<20}"
            f"{str(game.Date):<15}"
            f"{game.Arena:<25}"
        )

    print(colored("-" * WIDTH, Colors.BLUE))

    pause()

def display_player_game_stats(stats: list[Player_Game_Stats]) -> None:
    """Display player game statistics."""

    clear_screen()
    print_box_title("PLAYER GAME STATS")

    print(
        colored(
            f"{'GAME ID':<10}{'PLAYER ID':<12}{'NAME':<25}{'POINTS':<10}{'ASSISTS':<10}{'REB':<10}",
            Colors.YELLOW + Colors.BOLD
        )
    )

    print(colored("-" * WIDTH, Colors.BLUE))

    for stat in stats:
        print(
            f"{stat.Game_ID:<10}"
            f"{stat.Player_ID:<12}"
            f"{stat.Name:<25}"
            f"{stat.Points:<10}"
            f"{stat.Assists:<10}"
            f"{stat.Rebounds:<10}"
        )

    print(colored("-" * WIDTH, Colors.BLUE))

    pause()

# ============================================================
# Player Tab Actions 
# ============================================================
def player_menu(player_service: Player_Service) -> None:
    """Display the Player menu."""

    while True:
        clear_screen()
        print_box_title("PLAYER MENU")

        print("[1] View Players")
        print("[2] Search Player")
        print("[3] Add Player")
        print("[4] Delete Player")
        print("[5] Return To Home Page")

        choice = input(
            colored("\nSelect an option: ", Colors.WHITE)
        ).strip()


        # View All Players
        if choice == "1":

            players = player_service.get_all_players()

            display_players(players)


        # Search Player
        elif choice == "2":

            identifier = read_nonempty(
                "Enter Player Name or ID: "
            )

            try:
                player = player_service.search_player(identifier)

                print_section("PLAYER INFORMATION")
                print(f"Player ID : {player.Player_ID}")
                print(f"Name      : {player.Name}")
                print(f"Height    : {player.Height}")
                print(f"Weight    : {player.Weight}")
                print(f"College   : {player.College}")

            except ValueError as e:
                print_error(str(e))

            pause()


        # Add Player
        elif choice == "3":

            name = read_nonempty("Player Name: ")
            player_id = read_int("Player ID: ")
            weight = read_nonempty("Weight: ")
            height = read_nonempty("Height: ")
            college = read_nonempty("College: ")

            player = Player(
                Name=name,
                Player_ID=player_id,
                Weight=weight,
                Height=height,
                College=college
            )

            try:
                player_service.add_player(player)
                print_success("Player added successfully.")

            except ValueError as e:
                print_error(str(e))

            pause()


        # Delete Player
        elif choice == "4":

            identifier = read_nonempty(
                "Enter Player Name or ID: "
            )

            if confirm("Delete this player?"):

                try:
                    player_service.delete_player(identifier)
                    print_success(
                        "Player deleted successfully."
                    )

                except ValueError as e:
                    print_error(str(e))

            pause()


        # Return Home
        elif choice == "5":

            break


        else:
            print_error("Invalid option.")
            pause()
# ============================================================
# Team Tab Actions 
# ============================================================   
def team_menu(team_service: Team_Service) -> None:
    """Display the Team menu."""

    while True:
        clear_screen()
        print_box_title("TEAM MENU")

        print("[1] View Teams")
        print("[2] Search Teams")
        print("[3] Add Team")
        print("[4] Delete Team")
        print("[5] Return To Home Page")

        choice = input(
            colored("\nSelect an option: ", Colors.WHITE)
        ).strip()


        # View All Teams
        if choice == "1":

            teams = team_service.get_all_teams()

            display_teams(teams)


        # Search Team
        elif choice == "2":

            identifier = read_nonempty(
                "Enter Team Name or Team ID: "
            )

            try:
                team = team_service.search_team(identifier)

                print_section("TEAM INFORMATION")
                print(f"Team ID : {team.Team_ID}")
                print(f"Name    : {team.Name}")
                print(f"City    : {team.City}")
                print(f"State   : {team.State}")
                print(f"Arena   : {team.Arena}")
                print(f"Record  : {team.Record}")

            except ValueError as e:
                print_error(str(e))

            pause()


        # Add Team
        elif choice == "3":

            name = read_nonempty("Team Name: ")
            team_id = read_int("Team ID: ")
            city = read_nonempty("City: ")
            state = read_nonempty("State: ")
            arena = read_nonempty("Arena: ")
            record = read_nonempty(
                "Record (e.g. 0-0): "
            )

            team = Team(
                Name=name,
                Team_ID=team_id,
                City=city,
                State=state,
                Arena=arena,
                Record=record
            )

            try:
                team_service.add_team(team)
                print_success(
                    "Team added successfully."
                )

            except ValueError as e:
                print_error(str(e))

            pause()


        # Delete Team
        elif choice == "4":

            identifier = read_nonempty(
                "Enter Team Name or Team ID: "
            )

            if confirm("Delete this team?"):

                try:
                    team_service.delete_team(identifier)
                    print_success(
                        "Team deleted successfully."
                    )

                except ValueError as e:
                    print_error(str(e))

            pause()


        # Return Home
        elif choice == "5":

            break


        else:
            print_error("Invalid option.")
            pause()
# ============================================================
# Game Tab Actions 
# ============================================================   
def game_menu(game_service: Game_Service) -> None:
    """Display the Game menu."""

    while True:
        clear_screen()
        print_box_title("GAME MENU")

        print("[1] View Games")
        print("[2] Search Games")
        print("[3] Add Game")
        print("[4] Delete Game")
        print("[5] Return To Home Page")

        choice = input(
            colored("\nSelect an option: ", Colors.WHITE)
        ).strip()
        
        # View All Games
        if choice == "1":
            games = game_service.get_all_games()

            display_games(games)
        # Search Game
        elif choice == "2":
            identifier = read_nonempty(
                "Enter Game ID, Home Team, or Away Team: "
            )

            try:
                game = game_service.search_game(identifier)
                print_section("GAME INFORMATION")
                print(f"Game ID   : {game.Game_ID}")
                print(f"Home Team : {game.Home_Team}")
                print(f"Away Team : {game.Away_Team}")
                print(f"Date      : {game.Date}")
                print(f"Arena     : {game.Arena}")

            except ValueError as e:
                print_error(str(e))

            pause()
        # Add Game
        elif choice == "3":
            game_id = read_int("Game ID: ")
            home_team = read_nonempty("Home Team: ")
            away_team = read_nonempty("Away Team: ")
            game_date = datetime.strptime(
                read_nonempty("Game Date (YYYY-MM-DD): "),
                "%Y-%m-%d"
            ).date()
            arena = read_nonempty("Arena: ")
            try:
                game = Game(
                    Game_ID=game_id,
                    Home_Team=home_team,
                    Away_Team=away_team,
                    Date=game_date,
                    Arena=arena
                )
                game_service.add_game(game)
                print_success(
                    "Game added successfully."
                )
            except ValueError as e:
                print_error(str(e))

            pause()
        # Delete Game
        elif choice == "4":
            game_id = read_int(
                "Enter Game ID: "
            )
            if confirm("Delete this game?"):
                try:
                    game_service.delete_game(game_id)
                    print_success(
                        "Game deleted successfully."
                    )
                except ValueError as e:
                    print_error(str(e))
            pause()
        # Return Home
        elif choice == "5":

            break

        else:
            print_error("Invalid option.")
            pause()
# ============================================================
# Search Tab Actions 
# ============================================================   
def search_menu(
    player_stats_service: Player_Stats_Service,
    team_stats_service: Team_Stats_Service
) -> None:
    """Display the Search menu."""

    while True:
        clear_screen()
        print_box_title("SEARCH MENU")

        print("[1] Search Team")
        print("[2] Search Player Stats")
        print("[3] Return To Home Page")

        choice = input(colored("\nSelect an option: ", Colors.WHITE)).strip()

        if choice == "1":
            identifier = read_nonempty("Enter Team Name or Team ID: ")

            try:
                stats = team_stats_service.search_team_stats(identifier)

                print_section("TEAM STATISTICS")
                print(f"Team     : {stats['Team']}")
                print(f"Location : {stats['Location']}")
                print(f"Record   : {stats['Record']}")

            except ValueError as e:
                print_error(str(e))

            pause()

        elif choice == "2":
            identifier = read_nonempty("Enter Player Name or Player ID: ")

            try:
                stats = player_stats_service.search_player_stats(identifier)

                print_section("PLAYER STATISTICS")
                print(f"Name              : {stats['Name']}")
                print(f"College           : {stats['College']}")
                print(f"Points Average    : {stats['Points Average']:.2f}")
                print(f"Assist Average    : {stats['Assist Average']:.2f}")
                print(f"Rebound Average   : {stats['Rebound Average']:.2f}")

            except ValueError as e:
                print_error(str(e))

            pause()

        elif choice == "3":
            break

        else:
            print_error("Invalid option.")
            pause()
# ============================================================
# Main Menu
# ============================================================   
def main() -> None:
    """Run the NBA Stat Tracker terminal application."""

    # Create repositories
    player_repository = Player_Repository()
    team_repository = Team_Repository()
    game_repository = Game_Repository()
    player_game_stats_repository = Player_Game_Stats_Repository()


    # Create services
    player_service = Player_Service(
        player_repository
    )

    team_service = Team_Service(
        team_repository
    )

    game_service = Game_Service(
        game_repository
    )

    player_stats_service = Player_Stats_Service(
        player_repository,
        player_game_stats_repository
    )

    team_stats_service = Team_Stats_Service(
        team_repository
    )


    while True:
        clear_screen()

        print_box_title(
            "🏀 NBA STAT TRACKER 🏀",
            "Home Page"
        )

        print("🔍 [1] Player")
        print("🔍 [2] Team")
        print("🔍 [3] Game")
        print("🔍 [4] Stats")
        print("🔍 [5] Exit")


        choice = input(
            colored(
                "\nSelect an option ➜ ",
                Colors.BOLD + Colors.WHITE
            )
        ).strip()


        if choice == "5":
            clear_screen()

            print_box_title(
                "🏀 THANK YOU 🏀",
                "NBA Stat Tracker session ended"
            )

            print_success("Goodbye!")
            break


        try:

            if choice == "1":
                player_menu(
                    player_service
                )


            elif choice == "2":
                team_menu(
                    team_service
                )


            elif choice == "3":
                game_menu(
                    game_service
                )


            elif choice == "4":
                search_menu(
                    player_stats_service,
                    team_stats_service
                )


            else:
                print_error(
                    "Please choose a number from 1 through 5."
                )
                pause()


        except KeyboardInterrupt:
            print_warning(
                "Action cancelled."
            )
            pause()

        except Exception as error:
            print_error(
                f"Unexpected error: {error}"
            )
            pause()



if __name__ == "__main__":
    main()