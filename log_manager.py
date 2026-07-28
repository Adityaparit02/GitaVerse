"""
log_manager.py

Professional logging utility for the Bhagavad Gita Daily Verse application.
"""

import logging
import platform
import socket
import getpass
import sys
import time
from pathlib import Path
from datetime import datetime


class LogManager:
    """Handles application logging."""

    def __init__(self):

        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        self.logger = logging.getLogger("GitaVerse")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            file_handler = logging.FileHandler(
                log_dir / "app.log",
                encoding="utf-8"
            )

            formatter = logging.Formatter("%(message)s")

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

        self.start_time = None

    def line(self):
        self.logger.info("=" * 80)

    def blank(self):
        self.logger.info("")

    def start(self):

        self.start_time = time.perf_counter()

        self.line()
        self.logger.info("           BHAGAVAD GITA DAILY VERSE AUTOMATION")
        self.line()

        self.logger.info(
            f"Execution Started : "
            f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
        )

        self.line()

    def application_info(
        self,
        app_name,
        version,
        author
    ):

        self.logger.info(f"Application      : {app_name}")
        self.logger.info(f"Version          : {version}")
        self.logger.info(f"Author           : {author}")
        self.blank()

        self.logger.info(
            f"Operating System : "
            f"{platform.system()} {platform.release()}"
        )

        self.logger.info(
            f"Machine          : "
            f"{platform.machine()}"
        )

        self.logger.info(
            f"Processor        : "
            f"{platform.processor()}"
        )

        self.logger.info(
            f"Python Version   : "
            f"{platform.python_version()}"
        )

        self.logger.info(
            f"Python Executable: "
            f"{sys.executable}"
        )

        self.logger.info(
            f"Hostname         : "
            f"{socket.gethostname()}"
        )

        self.logger.info(
            f"User             : "
            f"{getpass.getuser()}"
        )

        self.line()

    def verse_loaded(
        self,
        verse_id,
        chapter,
        chapter_name,
        verse_number
    ):

        self.logger.info("VERSE INFORMATION")
        self.logger.info("-" * 80)

        self.logger.info(f"Current ID       : {verse_id}")
        self.logger.info(f"Chapter          : {chapter}")
        self.logger.info(f"Chapter Name     : {chapter_name}")
        self.logger.info(f"Verse            : {verse_number}")

        self.line()

    def formatting_completed(self):

        self.logger.info("Formatting       : SUCCESS")

        self.line()

    def email_sent(
        self,
        recipient,
        subject
    ):

        self.logger.info("EMAIL STATUS")
        self.logger.info("-" * 80)

        self.logger.info("Status           : SUCCESS")
        self.logger.info(f"Recipient        : {recipient}")
        self.logger.info(f"Subject          : {subject}")

        self.line()

    def state_updated(
        self,
        previous,
        current
    ):

        self.logger.info("STATE INFORMATION")
        self.logger.info("-" * 80)

        self.logger.info(f"Previous ID      : {previous}")
        self.logger.info(f"Current ID       : {current}")

        self.line()

    def warning(self, message):

        self.logger.warning(f"WARNING : {message}")

    def error(self, message):

        self.logger.error(f"ERROR : {message}")

        self.line()

    def finish(
        self,
        success=True
    ):

        elapsed = time.perf_counter() - self.start_time

        self.logger.info(
            f"Execution Time   : "
            f"{elapsed:.2f} Seconds"
        )

        self.logger.info(
            f"Status           : "
            f"{'SUCCESS' if success else 'FAILED'}"
        )

        self.logger.info(
            f"Execution Ended  : "
            f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
        )

        self.line()
        self.blank()