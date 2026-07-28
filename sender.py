"""
sender.py

Handles sending emails.
"""
import logger
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import (
    SENDER_EMAIL,
    APP_PASSWORD,
    RECEIVER_EMAIL
)


class EmailSender:
    """Send emails using Gmail SMTP."""

    def send(self, subject: str, body: str) -> bool:
        """
        Send an email.

        Args:
            subject (str): Email subject.
            body (str): Email body.

        Returns:
            bool: True if email sent successfully, otherwise False.
        """

        try:
            message = MIMEMultipart()

            message["From"] = SENDER_EMAIL
            message["To"] = RECEIVER_EMAIL
            message["Subject"] = subject

            message.attach(
                MIMEText(body, "html", "utf-8")
            )

            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

                smtp.starttls()
                print(f"Sender: {SENDER_EMAIL}")
                print(f"Password Length: {len(APP_PASSWORD) if APP_PASSWORD else 0}")   
                smtp.login(
                    SENDER_EMAIL,
                    APP_PASSWORD
                )

                smtp.send_message(message)

            return True

        except Exception as error:

            print(f"Error: {error}")
            return False