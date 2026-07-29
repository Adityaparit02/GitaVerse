from sender import EmailSender

sender = EmailSender()

success = sender.send(
    subject="Bhagavad Gita Test",
    body="जय श्रीकृष्ण 🙏\n\nThis is a test email from GitaVerse."
)

print(success)