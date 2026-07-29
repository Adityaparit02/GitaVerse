###############################################################################
#                                                                             #
#                           G I T A V E R S E                                 #
#                 Daily Bhagavad Gita Verse Email Automation                  #
#                                                                             #
###############################################################################
# Project Name : GitaVerse
# File Name    : <state_manager.py>
#
# Author       : Aditya Namdeo Parit
# GitHub       : https://github.com/Adityaparit02/GitaVerse
# Created On   : 28 July 2026
# Last Updated : 29 July 2026
# Version      : 1.0.0
#
# Description  :
# -----------------------------------------------------------------------------
# Maintains the application's current verse progress and updates the state
# after every successful email delivery.

# Features :
# -----------------------------------------------------------------------------
# • Daily Bhagavad Gita Verse Automation
# • HTML Email Generation
# • Multiple Subscriber Support
# • GitHub Actions Automation
# • Automatic Verse Progression
# • State Management
# • Logging & Error Handling
#
# Copyright (c) 2026 Aditya Namdeo Parit
###############################################################################

"""
state_manager.py

Handles reading and updating the application's state.
"""

import json
from pathlib import Path


class StateManager:
    """Manage the current verse state."""

    def __init__(self, state_path: str):
        """
        Initialize the state manager.

        Args:
            state_path (str): Path to state JSON file.
        """

        self.state_path = Path(state_path)
        self.state = self._load_state()

    def _load_state(self) -> dict:
        """
        Load state JSON.
        """

        try:
            with open(self.state_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError(
                f"State file not found: {self.state_path}"
            )

        except json.JSONDecodeError as error:
            raise ValueError(
                f"Invalid state JSON: {error}"
            )

    def _save_state(self) -> None:
        """
        Save state JSON.
        """

        with open(self.state_path, "w", encoding="utf-8") as file:
            json.dump(
                self.state,
                file,
                indent=4,
                ensure_ascii=False
            )

    def get_current_id(self) -> int:
        """
        Return current verse ID.
        """

        return self.state["current_id"]

    def set_current_id(self, verse_id: int) -> None:
        """
        Set current verse ID.
        """

        self.state["current_id"] = verse_id
        self._save_state()

    def increment(self, total_verses: int) -> None:
        """
        Move to the next verse.

        If the last verse is reached,
        restart from verse 1.
        """

        current = self.get_current_id()

        if current >= total_verses:
            self.state["current_id"] = 1
        else:
            self.state["current_id"] += 1

        self._save_state()