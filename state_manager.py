###############################################################################
#                                                                             #
#                           G I T A V E R S E                                 #
#                 Daily Bhagavad Gita Verse Email Automation                  #
#                                                                             #
###############################################################################
# Project Name : GitaVerse
# File Name    : state_manager.py
#
# Author       : Aditya Namdeo Parit
# GitHub       : https://github.com/Adityaparit02/GitaVerse
# Created On   : 28 July 2026
# Last Updated : 18 August 2026
# Version      : 1.1.0
#
# Description  :
# -----------------------------------------------------------------------------
# Maintains the current chapter and verse position of the GitaVerse
# application and automatically moves between chapters.
#
# Features :
# -----------------------------------------------------------------------------
# • Chapter-wise State Management
# • Automatic Verse Progression
# • Automatic Chapter Transition
# • Backward Compatibility
# • Persistent JSON State
#
# Copyright (c) 2026 Aditya Namdeo Parit
###############################################################################

"""
state_manager.py

Handles reading and updating the application's chapter and verse state.
"""

import json
from pathlib import Path


class StateManager:
    """Manage the current Bhagavad Gita chapter and verse state."""

    def __init__(self, state_path: str):

        self.state_path = Path(state_path)
        self.state = self._load_state()

    def _load_state(self) -> dict:
        """
        Load state JSON.

        Supports both the old format:

            {
                "current_id": 15
            }

        and the new format:

            {
                "chapter": 1,
                "verse": 15
            }
        """

        try:

            with open(
                self.state_path,
                "r",
                encoding="utf-8"
            ) as file:

                state = json.load(file)

        except FileNotFoundError:

            raise FileNotFoundError(
                f"State file not found: {self.state_path}"
            )

        except json.JSONDecodeError as error:

            raise ValueError(
                f"Invalid state JSON: {error}"
            )

        # Backward compatibility
        if (
            "chapter" not in state
            and "verse" not in state
            and "current_id" in state
        ):

            state = {
                "chapter": 1,
                "verse": state["current_id"]
            }

            self.state = state
            self._save_state()

        return state

    def _save_state(self) -> None:
        """Save current state to JSON."""

        self.state_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.state_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.state,
                file,
                indent=4,
                ensure_ascii=False
            )

    def get_current_chapter(self) -> int:
        """Return the current chapter number."""

        return self.state["chapter"]

    def get_current_verse(self) -> int:
        """Return the current verse number."""

        return self.state["verse"]

    def get_current_position(self) -> tuple[int, int]:
        """
        Return current chapter and verse.

        Returns:
            tuple[int, int]:
                (chapter, verse)
        """

        return (
            self.get_current_chapter(),
            self.get_current_verse()
        )

    def set_position(
        self,
        chapter: int,
        verse: int
    ) -> None:
        """
        Set current chapter and verse.
        """

        self.state["chapter"] = chapter
        self.state["verse"] = verse

        self._save_state()

    def move_to_next(
        self,
        reader
    ) -> None:
        """
        Move to the next verse.

        If the current chapter is finished,
        move to the first verse of the next chapter.

        If the final available chapter is finished,
        restart from the first verse of the first chapter.
        """

        current_chapter = self.get_current_chapter()
        current_verse = self.get_current_verse()

        total_verses = reader.get_total_verses(
            current_chapter
        )

        # More verses remain in current chapter
        if current_verse < total_verses:

            self.state["verse"] = current_verse + 1

        else:

            # Move to next chapter
            next_chapter = reader.get_next_chapter(
                current_chapter
            )

            if next_chapter is not None:

                first_verse = reader.get_first_verse_number(
                    next_chapter
                )

                self.state["chapter"] = next_chapter
                self.state["verse"] = first_verse

            else:

                # All available chapters completed.
                # Restart from Chapter 1.
                first_chapter = (
                    reader.get_available_chapters()[0]
                )

                first_verse = reader.get_first_verse_number(
                    first_chapter
                )

                self.state["chapter"] = first_chapter
                self.state["verse"] = first_verse

        self._save_state()