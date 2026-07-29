###############################################################################
#                                                                             #
#                           G I T A V E R S E                                 #
#                 Daily Bhagavad Gita Verse Email Automation                  #
#                                                                             #
###############################################################################
# Project Name : GitaVerse
# File Name    : <subscriber_manager.py>
#
# Author       : Aditya Namdeo Parit
# GitHub       : https://github.com/Adityaparit02/GitaVerse
# Created On   : 28 July 2026
# Last Updated : 29 July 2026
# Version      : 1.0.0
#
# Description  :
# -----------------------------------------------------------------------------
# Loads and manages subscriber information stored in subscribers.json.
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
import json


class SubscriberManager:
    """Manages GitaVerse subscribers."""

    def __init__(self, file_path="data/subscribers.json"):
        self.file_path = file_path

    def get_all(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            return data.get("subscribers", [])

        except Exception as e:
            print(f"Subscriber Error: {e}")
            return []