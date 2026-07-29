###############################################################################
#                                                                             #
#                           G I T A V E R S E                                 #
#                 Daily Bhagavad Gita Verse Email Automation                  #
#                                                                             #
###############################################################################
# Project Name : GitaVerse
# File Name    : <reader.py>
#
# Author       : Aditya Namdeo Parit
# GitHub       : https://github.com/Adityaparit02/GitaVerse
# Created On   : 28 July 2026
# Last Updated : 29 July 2026
# Version      : 1.0.0
#
# Description  :
# -----------------------------------------------------------------------------
# Reads Bhagavad Gita chapter JSON files and returns the requested verse
# according to the current application state.
#
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
reader.py

Handles reading Bhagavad Gita verses from JSON.
"""

import json
from pathlib import Path


class GitaReader:
    """Read Bhagavad Gita verses from a JSON database."""

    def __init__(self, json_path: str):
        """
        Initialize the reader.

        Args:
            json_path (str): Path to Bhagavad Gita JSON file.
        """

        self.json_path = Path(json_path)
        self.data = self._load_json()

        if "verses" not in self.data:
            raise KeyError("'verses' key not found in JSON.")

        self.verses = self.data["verses"]

        # Dictionary for fast O(1) lookup
        self.verse_index = {
            verse["id"]: verse
            for verse in self.verses
        }

    def _load_json(self) -> dict:
        """
        Load the JSON file.

        Returns:
            dict: Parsed JSON data.
        """

        try:
            with open(self.json_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError(
                f"JSON file not found: {self.json_path}"
            )

        except json.JSONDecodeError as error:
            raise ValueError(
                f"Invalid JSON: {error}"
            )

    def get_verse_by_id(self, verse_id: int) -> dict | None:
        """
        Return verse by its unique ID.

        Args:
            verse_id (int): Verse ID.

        Returns:
            dict | None
        """

        return self.verse_index.get(verse_id)

    def verse_exists(self, verse_id: int) -> bool:
        """
        Check whether a verse exists.
        """

        return verse_id in self.verse_index

    def get_all_verses(self) -> list:
        """
        Return all verses.
        """

        return self.verses

    def get_total_verses(self) -> int:
        """
        Return number of verses currently loaded.
        """

        return len(self.verses)

    def get_book_information(self) -> dict:
        """
        Return book metadata.
        """

        return {
            "book": self.data.get("book"),
            "chapters": self.data.get("total_chapters"),
            "verses": self.data.get("total_verses"),
            "language": self.data.get("language")
        }