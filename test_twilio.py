from twilio.rest import Client

from config import (
    ACCOUNT_SID,
    AUTH_TOKEN,
    TWILIO_NUMBER,
    DESTINATION_NUMBER,
)

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="जय श्रीकृष्ण 🙏 This is a test SMS from Bhagavad Gita Automation.",
    from_=TWILIO_NUMBER,
    to=DESTINATION_NUMBER,
)

print("Message SID:", message.sid)
print("Status:", message.status)