from __future__ import annotations

import os
from decimal import Decimal, InvalidOperation
from typing import Callable

from Model.Game_Model import Game
from Model.Game_Stats import Game_Stats
from Model.Player_Game_Stats_Model import Player_Game_Stats
from Model.Player_Model import Player
from Model.Player_Stats_Model import Player_Stats
from Model.Team_Model import Team
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
