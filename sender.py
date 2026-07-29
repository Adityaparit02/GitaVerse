###############################################################################
#                                                                             #
#                           G I T A V E R S E                                 #
#                 Daily Bhagavad Gita Verse Email Automation                  #
#                                                                             #
###############################################################################
# Project Name : GitaVerse
# File Name    : <sender.py>
#
# Author       : Aditya Namdeo Parit
# GitHub       : https://github.com/Adityaparit02/GitaVerse
# Created On   : 28 July 2026
# Last Updated : 29 July 2026
# Version      : 1.0.0
#
# Description  :
# -----------------------------------------------------------------------------
# Handles SMTP authentication and securely sends HTML formatted Bhagavad Gita
# emails individually to all registered subscribers.
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