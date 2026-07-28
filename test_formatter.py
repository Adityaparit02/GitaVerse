from reader import GitaReader
from formatter import Formatter

reader = GitaReader("data/chapter_01.json")

verse = reader.get_verse_by_id(1)

formatter = Formatter()

message = formatter.format_message(verse)

print(message)