###############################################################################
#                                                                             #
#                           G I T A V E R S E                                 #
#                 Daily Bhagavad Gita Verse Email Automation                  #
#                                                                             #
###############################################################################
# Project Name : GitaVerse
# File Name    : <config.py>
#
# Author       : Aditya Namdeo Parit
# GitHub       : https://github.com/Adityaparit02/GitaVerse
# Created On   : 28 July 2026
# Last Updated : 29 July 2026
# Version      : 1.0.0
#
# Description  :
# -----------------------------------------------------------------------------
# Loads environment variables and application configuration required by
# the GitaVerse project.
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
# 
###############################################################################


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