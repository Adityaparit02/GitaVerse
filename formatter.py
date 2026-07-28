from pathlib import Path


class Formatter:
    """
    Generates HTML email by loading the template
    and replacing placeholders.
    """

    def __init__(self):
        self.template_path = Path("templates/email_template.html")

    def load_template(self):
        """
        Load HTML template.
        """
        with open(self.template_path, "r", encoding="utf-8") as f:
            return f.read()

    def create_keyword_badges(self, keywords):
        """
        Convert keyword list into HTML badges.

        Example:
        ["Duty","Courage"]

        =>
        <span class="badge">Duty</span>
        <span class="badge">Courage</span>
        """

        if not keywords:
            return ""

        badges = []

        for word in keywords:
            badges.append(
                f'<span class="badge">{word}</span>'
            )

        return "\n".join(badges)

    def format_html(self, verse_data):
        """
        Replace all placeholders inside the template.

        Parameters
        ----------
        verse_data : dict

        Returns
        -------
        str
            Final HTML
        """

        html = self.load_template()

        replacements = {

            "{chapter}":
                str(verse_data.get("chapter", "")),

            "{chapter_name}":
                verse_data.get("chapter_name", ""),

            "{verse_number}":
                str(verse_data.get("verse", "")),

            "{sanskrit}":
                verse_data.get("sanskrit", "").replace("\n", "<br>"),

            "{transliteration}":
                verse_data.get("transliteration", "").replace("\n", "<br>"),

            "{english}":
                verse_data.get("english", "").replace("\n", "<br>"),

            "{hindi}":
                verse_data.get("hindi", "").replace("\n", "<br>"),

            "{marathi}":
                verse_data.get("marathi", "").replace("\n", "<br>"),

            "{word_meaning}":
                verse_data.get("word_meaning", "").replace("\n", "<br>"),

            "{reflection}":
                verse_data.get("reflection", "").replace("\n", "<br>"),

            "{keywords}":
                self.create_keyword_badges(
                    verse_data.get("keywords", [])
                )

        }

        for key, value in replacements.items():
            html = html.replace(key, value)

        return html


if __name__ == "__main__":

    sample = {

        "chapter": 1,

        "chapter_name": "Arjuna Vishada Yoga",

        "verse_number": 1,

        "sanskrit":
        "धृतराष्ट्र उवाच।",

        "transliteration":
        "dhṛtarāṣṭra uvāca",

        "english":
        "Dhritarashtra said...",

        "hindi":
        "धृतराष्ट्र ने कहा...",

        "marathi":
        "धृतराष्ट्र म्हणाला...",

        "word_meaning":
        "Dhritarashtra = King of Hastinapur",

        "reflection":
        "Every great journey begins with a sincere question.",

        "keywords":
        [
            "Duty",
            "Wisdom",
            "Karma",
            "Devotion",
            "Dharma"
        ]

    }

    formatter = Formatter()

    html = formatter.format_html(sample)

    with open("preview.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("preview.html generated successfully.")