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