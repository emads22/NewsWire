import os
import yagmail
from datetime import datetime
# import pandas as pd
from constants import SENDER, PASSWORD, CONTACT_FILE


def send_email(receiver, subject, body):
    # Creating an SMTP connection with yagmail using sender's credentials
    yag = yagmail.SMTP(user=SENDER, password=PASSWORD)

    # Sending the email to the recipient
    yag.send(to=receiver, subject=subject, contents=body)

    # Printing a confirmation message after the email is sent
    print(f"\n--- Email sent successfully to: {receiver} ---\n")


def main():
    # Read the contacts file into a DataFrame
    contacts_df = pd.read_csv(CONTACTS_FILE)

    # Iterate through each row in the DataFrame
    for _, row in contacts_df.iterrows():
        # Extracting the receiver's email from the current row
        receiver = row['Email']

        # Defining the subject line of the email
        subject = f"GREETING FROM {SENDER}!"

        # Defining the contents of the email
        contents = f"""
        Hello {row['Name']},
        It's {datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")}.
        Here is the content of the email! 
        :)
        """

        # Sending email to the current recipient
        send_email(receiver, subject, contents)


if __name__ == "__main__":
    receiver = "dofef22481@morxin.com"

    # Defining the subject line of the email
    subject = f"GREETING FROM {SENDER}!"

    # Defining the contents of the email
    contents = f"""
    Hello there,
    It's {datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")}.
    Here is the content of the email! 
    :)
    """

    # Sending email to the current recipient
    send_email(receiver, subject, contents)


