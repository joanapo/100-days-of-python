import smtplib
import os
from dotenv import load_dotenv

load_dotenv() # access the environment variables

class EmailManager:
    def __init__(self):
        self.connection = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"], 587)
        self.email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_EMAIL_PASSWORD"]

    def send_email(self, recipient, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.password)
            self.connection.sendmail(from_addr=self.email,
                                     to_addrs=recipient,
                                     msg=f"Subject:Amazon Price Alert!\n\n{email_body}".encode("utf-8"))