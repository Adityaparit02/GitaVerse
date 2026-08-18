###############################################################################
#                                                                             #
#                           G I T A V E R S E                                 #
#                 Daily Bhagavad Gita Verse Email Automation                  #
#                                                                             #
###############################################################################
# Project Name : GitaVerse
# File Name    : main.py
#
# Author       : Aditya Namdeo Parit
# GitHub       : https://github.com/Adityaparit02/GitaVerse
# Created On   : 28 July 2026
# Last Updated : 18 August 2026
# Version      : 1.1.0
#
# Description  :
# -----------------------------------------------------------------------------
# Main entry point of the GitaVerse application.
#
# Coordinates:
# • Chapter and verse reading
# • State management
# • HTML formatting
# • Subscriber management
# • Email delivery
# • Application logging
# • Automatic chapter and verse progression
#
# Copyright (c) 2026 Aditya Namdeo Parit
###############################################################################

"""
main.py

Main entry point of the Bhagavad Gita Daily Verse application.
"""

from reader import GitaReader
from state_manager import StateManager
from formatter import Formatter
from sender import EmailSender
from log_manager import LogManager
from subscriber_manager import SubscriberManager


def main() -> None:
    """Execute the complete daily verse workflow."""

    # -------------------------------------------------------------------------
    # Initialize modules
    # -------------------------------------------------------------------------

    reader = GitaReader("data")

    state = StateManager(
        "state/current_verse.json"
    )

    formatter = Formatter()
    sender = EmailSender()
    subscriber = SubscriberManager()
    log = LogManager()

    # -------------------------------------------------------------------------
    # Start logging
    # -------------------------------------------------------------------------

    log.start()

    log.application_info(
        app_name="GitaVerse",
        version="1.1.0",
        author="Aditya Namdeo Parit"
    )

    # -------------------------------------------------------------------------
    # Get current chapter and verse
    # -------------------------------------------------------------------------

    current_chapter = state.get_current_chapter()
    current_verse = state.get_current_verse()

    # -------------------------------------------------------------------------
    # Check whether chapter exists
    # -------------------------------------------------------------------------

    if not reader.chapter_exists(current_chapter):

        log.error(
            f"Chapter {current_chapter} not found."
        )

        log.finish(False)

        return

    # -------------------------------------------------------------------------
    # Get current verse
    # -------------------------------------------------------------------------

    verse = reader.get_verse(
        current_chapter,
        current_verse
    )

    if verse is None:

        log.error(
            f"Chapter {current_chapter}, "
            f"Verse {current_verse} not found."
        )

        log.finish(False)

        return

    # -------------------------------------------------------------------------
    # Log verse information
    # -------------------------------------------------------------------------

    log.verse_loaded(
        verse_id=verse.get("id", current_verse),
        chapter=verse["chapter"],
        chapter_name=verse["chapter_name"],
        verse_number=verse["verse"]
    )

    # -------------------------------------------------------------------------
    # Get subscribers
    # -------------------------------------------------------------------------

    receivers = subscriber.get_all()

    if not receivers:

        log.error(
            "No subscribers found."
        )

        log.finish(False)

        return

    # -------------------------------------------------------------------------
    # Format HTML email
    # -------------------------------------------------------------------------

    message = formatter.format_html(verse)

    log.formatting_completed()

    # -------------------------------------------------------------------------
    # Email subject
    # -------------------------------------------------------------------------

    subject = (
        f"Bhagavad Gita | "
        f"Chapter {verse['chapter']} "
        f"Verse {verse['verse']}"
    )

    # -------------------------------------------------------------------------
    # Send email
    # -------------------------------------------------------------------------

    success = sender.send(
        subject,
        message,
        receivers
    )

    # -------------------------------------------------------------------------
    # Update state only after successful email
    # -------------------------------------------------------------------------

    if success:

        previous_chapter = current_chapter
        previous_verse = current_verse

        state.move_to_next(reader)

        new_chapter = state.get_current_chapter()
        new_verse = state.get_current_verse()

        # -------------------------------------------------------------
        # Log email status
        # -------------------------------------------------------------

        log.email_sent(
            recipient=f"{len(receivers)} subscriber(s)",
            subject=subject
        )

        # -------------------------------------------------------------
        # Log state update
        # -------------------------------------------------------------

        log.state_updated(
            previous=(
                f"Chapter {previous_chapter}, "
                f"Verse {previous_verse}"
            ),
            current=(
                f"Chapter {new_chapter}, "
                f"Verse {new_verse}"
            )
        )

        log.finish(True)

    else:

        log.error(
            "Email sending failed. "
            "State was not updated."
        )

        log.finish(False)


if __name__ == "__main__":
    main()