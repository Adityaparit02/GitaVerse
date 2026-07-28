"""
config.py

Application configuration.
"""

import os

SENDER_EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAILS = [
    email.strip()
    for email in os.getenv("RECEIVER", "").split(",")
    if email.strip()
]