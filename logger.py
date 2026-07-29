###############################################################################
#                                                                             #
#                           G I T A V E R S E                                 #
#                 Daily Bhagavad Gita Verse Email Automation                  #
#                                                                             #
###############################################################################
# Project Name : GitaVerse
# File Name    : <logger.py>
#
# Author       : Aditya Namdeo Parit
# GitHub       : https://github.com/Adityaparit02/GitaVerse
# Created On   : 28 July 2026
# Last Updated : 29 July 2026
# Version      : 1.0.0
#
# Description  :
# -----------------------------------------------------------------------------
# Provides centralized logging utilities used throughout the project.
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
logger.py

Application logging configuration.
"""

import logging
from pathlib import Path


class Logger:
    """Configure application logging."""

    def __init__(self):

        log_directory = Path("logs")
        log_directory.mkdir(exist_ok=True)

        log_file = log_directory / "app.log"

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S",
            force=True
        )

        self.logger = logging.getLogger("GitaVerse")

    def info(self, message: str) -> None:
        """Write an info log."""
        self.logger.info(message)

    def error(self, message: str) -> None:
        """Write an error log."""
        self.logger.error(message)

    def warning(self, message: str) -> None:
        """Write a warning log."""
        self.logger.warning(message)