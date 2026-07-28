"""
config.py

Application configuration.
"""

import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("PASSWORD")

RECEIVER_EMAILS = [
    email.strip()
    for email in os.getenv("RECEIVER", "").split(",")
    if email.strip()
]

print("EMAIL:", SENDER_EMAIL)
print("PASSWORD LENGTH:", len(APP_PASSWORD) if APP_PASSWORD else 0)