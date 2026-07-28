"""
sender.py

Handles sending emails.
"""

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import (
    SENDER_EMAIL,
    APP_PASSWORD
)


class EmailSender:
    """Send emails using Gmail SMTP."""

    def send(self, subject: str, body: str, receivers: list[str]) -> bool:
        """
        Send an email to all subscribers individually.

        Args:
            subject (str): Email subject.
            body (str): HTML email body.
            receivers (list[str]): List of recipient email addresses.

        Returns:
            bool: True if all emails are sent successfully, otherwise False.
        """

        if not receivers:
            print("No subscribers found.")
            return False

        try:

            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

                smtp.starttls()

                smtp.login(
                    SENDER_EMAIL,
                    APP_PASSWORD
                )

                for receiver in receivers:

                    message = MIMEMultipart()

                    message["From"] = SENDER_EMAIL
                    message["To"] = receiver
                    message["Subject"] = subject

                    message.attach(
                        MIMEText(body, "html", "utf-8")
                    )

                    smtp.sendmail(
                        SENDER_EMAIL,
                        receiver,
                        message.as_string()
                    )

                    print(f"✓ Email sent to {receiver}")

            return True

        except Exception as error:

            print(f"Error: {error}")
            return False