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

    # Initialize modules
    reader = GitaReader("data/Chapter_01.json")
    state = StateManager("state/current_verse.json")
    formatter = Formatter()
    sender = EmailSender()
    log = LogManager()
    subscriber = SubscriberManager()

    # Start logging
    log.start()

    log.application_info(
        app_name="GitaVerse",
        version="1.0.0",
        author="Aditya Namdeo Parit"
    )

    # Get current verse
    current_id = state.get_current_id()

    verse = reader.get_verse_by_id(current_id)

    if verse is None:
        log.error(f"Verse ID {current_id} not found.")
        log.finish(False)
        return

    # Log verse details
    log.verse_loaded(
        verse_id=current_id,
        chapter=verse["chapter"],
        chapter_name=verse["chapter_name"],
        verse_number=verse["verse"]
    )

    # Load subscribers
    receivers = subscriber.get_all()

    if not receivers:
        log.error("No subscribers found.")
        log.finish(False)
        return

    # Format HTML email
    message = formatter.format_html(verse)

    log.formatting_completed()

    # Email subject
    subject = (
        f"Bhagavad Gita | "
        f"Chapter {verse['chapter']} "
        f"Verse {verse['verse']}"
    )

    # Send email
    success = sender.send(
        subject,
        message,
        receivers
    )

    if success:

        previous = current_id

        # Move to next verse
        state.increment(reader.get_total_verses())

        log.email_sent(
            recipient=f"{len(receivers)} Subscribers",
            subject=subject
        )

        log.state_updated(
            previous=previous,
            current=state.get_current_id()
        )

        log.finish(True)

    else:

        log.error(
            "Email sending failed. State was not updated."
        )

        log.finish(False)


if __name__ == "__main__":
    main()