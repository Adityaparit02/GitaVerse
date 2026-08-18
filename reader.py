###############################################################################
#                                                                             #
#                           G I T A V E R S E                                 #
#                 Daily Bhagavad Gita Verse Email Automation                  #
#                                                                             #
###############################################################################
# Project Name : GitaVerse
# File Name    : reader.py
#
# Author       : Aditya Namdeo Parit
# GitHub       : https://github.com/Adityaparit02/GitaVerse
# Created On   : 28 July 2026
# Last Updated : 18 August 2026
# Version      : 1.1.0
#
# Description  :
# -----------------------------------------------------------------------------
# Reads Bhagavad Gita verses from multiple chapter JSON files and provides
# chapter-wise and verse-wise access to the application.
#
# Features :
# -----------------------------------------------------------------------------
# • Multi-Chapter JSON Support
# • Automatic Chapter Detection
# • Fast Verse Lookup
# • Chapter-wise Verse Progression
# • Automatic Chapter Transition
# • JSON Validation
#
# Copyright (c) 2026 Aditya Namdeo Parit
###############################################################################

"""
reader.py

Handles reading Bhagavad Gita verses from multiple JSON files.
"""

import json
from pathlib import Path


class GitaReader:
    """Read Bhagavad Gita verses from multiple chapter JSON files."""

    def __init__(self, data_directory: str):
        """
        Initialize the Gita reader.

        Args:
            data_directory (str):
                Directory containing Chapter_01.json,
                Chapter_02.json, etc.
        """

        self.data_directory = Path(data_directory)

        if not self.data_directory.exists():
            raise FileNotFoundError(
                f"Data directory not found: {self.data_directory}"
            )

        self.chapters = self._load_all_chapters()

        if not self.chapters:
            raise FileNotFoundError(
                f"No chapter JSON files found in {self.data_directory}"
            )

    def _load_all_chapters(self) -> dict:
        """
        Load all Chapter_XX.json files.

        Returns:
            dict:
                Dictionary containing chapter data.
        """

        chapters = {}

        json_files = sorted(
            self.data_directory.glob("Chapter_*.json")
        )

        for json_file in json_files:

            try:

                with open(
                    json_file,
                    "r",
                    encoding="utf-8"
                ) as file:

                    data = json.load(file)

            except json.JSONDecodeError as error:

                raise ValueError(
                    f"Invalid JSON in {json_file}: {error}"
                )

            if "verses" not in data:
                raise KeyError(
                    f"'verses' key not found in {json_file}"
                )

            chapter_number = self._extract_chapter_number(
                json_file
            )

            self._validate_verses(
                data["verses"],
                json_file
            )

            chapters[chapter_number] = {
                "data": data,
                "verses": data["verses"],
                "verse_index": {
                    verse["verse"]: verse
                    for verse in data["verses"]
                }
            }

        return dict(sorted(chapters.items()))

    def _extract_chapter_number(self, file_path: Path) -> int:
        """
        Extract chapter number from filename.

        Example:
            Chapter_01.json → 1
            Chapter_02.json → 2
        """

        try:

            chapter_number = int(
                file_path.stem.split("_")[1]
            )

            return chapter_number

        except (IndexError, ValueError):

            raise ValueError(
                f"Invalid chapter filename: {file_path.name}. "
                f"Expected format: Chapter_01.json"
            )

    def _validate_verses(
        self,
        verses: list,
        file_path: Path
    ) -> None:
        """
        Validate verse structure.
        """

        if not isinstance(verses, list):
            raise TypeError(
                f"'verses' must be a list in {file_path}"
            )

        for verse in verses:

            if "verse" not in verse:
                raise KeyError(
                    f"'verse' key missing in {file_path}"
                )

    def get_verse(
        self,
        chapter: int,
        verse_number: int
    ) -> dict | None:
        """
        Return a specific verse.

        Args:
            chapter (int):
                Chapter number.

            verse_number (int):
                Verse number within the chapter.

        Returns:
            dict | None:
                Verse information if found.
        """

        chapter_data = self.chapters.get(chapter)

        if chapter_data is None:
            return None

        return chapter_data["verse_index"].get(
            verse_number
        )

    def chapter_exists(self, chapter: int) -> bool:
        """
        Check whether a chapter exists.
        """

        return chapter in self.chapters

    def verse_exists(
        self,
        chapter: int,
        verse_number: int
    ) -> bool:
        """
        Check whether a verse exists.
        """

        return (
            self.get_verse(
                chapter,
                verse_number
            )
            is not None
        )

    def get_total_verses(
        self,
        chapter: int
    ) -> int:
        """
        Return the number of verses in a chapter.
        """

        chapter_data = self.chapters.get(chapter)

        if chapter_data is None:
            return 0

        return len(chapter_data["verses"])

    def get_available_chapters(self) -> list[int]:
        """
        Return all available chapter numbers.
        """

        return list(self.chapters.keys())

    def get_next_chapter(
        self,
        current_chapter: int
    ) -> int | None:
        """
        Return the next available chapter.

        If there is no next chapter, return None.
        """

        chapters = self.get_available_chapters()

        for chapter in chapters:

            if chapter > current_chapter:
                return chapter

        return None

    def get_first_verse_number(
        self,
        chapter: int
    ) -> int:
        """
        Return the first verse number of a chapter.
        """

        chapter_data = self.chapters.get(chapter)

        if chapter_data is None:
            return 0

        verses = chapter_data["verses"]

        if not verses:
            return 0

        return min(
            verse["verse"]
            for verse in verses
        )

    def get_book_information(self) -> dict:
        """
        Return information about loaded chapters.
        """

        total_verses = sum(
            len(chapter["verses"])
            for chapter in self.chapters.values()
        )

        return {
            "book": "Bhagavad Gita",
            "chapters_loaded": len(self.chapters),
            "available_chapters":
                self.get_available_chapters(),
            "total_verses_loaded":
                total_verses
        }