import logging
import yagmail
from config import *


class EmailService:
    """
    A class to handle sending emails using yagmail.

    Attributes:
        sender (str): The sender's email address.
        password (str): The sender's email password.
        receiver (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body content of the email.
    """

    def __init__(self, receiver: str, subject: str, body: str, sender: str = SENDER, password: str = PASSWORD) -> None:
        """
        Initializes an EmailService object with the specified parameters.

        Args:
            receiver (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body content of the email.
            sender (str, optional): The sender's email address (default is the value of SENDER).
            password (str, optional): The sender's email password (default is the value of PASSWORD).
        """
        self.sender = sender
        self.password = password
        self.receiver = receiver
        self.subject = subject
        self.body = body

    def send(self) -> None:
        """
        Sends the email to the recipient.

        Raises:
            Exception: If an error occurs while sending the email.
        """
        try:
            with yagmail.SMTP(user=self.sender, password=self.password) as yag_connection:
                # Sending the email to the recipient
                yag_connection.send(to=self.receiver,
                                    subject=self.subject,
                                    contents=self.body)
                logging.info(f'Email sent successfully to "{
                             self.receiver}" with subject: "{self.subject}"')
        except Exception as e:
            logging.error(f"Failure to send email: {e}", exc_info=True)
