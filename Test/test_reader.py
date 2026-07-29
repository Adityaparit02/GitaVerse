from reader import GitaReader

reader = GitaReader("data/chapter_01.json")

print(reader.get_book_information())

print()

print(reader.get_total_verses())

print()

verse = reader.get_verse_by_id(1)

print(verse["chapter_name"])
print(verse["verse"])

print()

print(verse["sanskrit"])

print()

print(verse["english"])

print()

print(verse["hindi"])

print()

print(verse["marathi"])