"""
config.py

Application configuration.
"""

import os

SENDER_EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER")