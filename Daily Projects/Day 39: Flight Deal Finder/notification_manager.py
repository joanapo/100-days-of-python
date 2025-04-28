import os
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

    def send_message(self, body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_PHONE"]}',
            body=body,
            to=f'whatsapp:{os.environ["TWILIO_MY_PHONE"]}'
        )
        print(message.sid)