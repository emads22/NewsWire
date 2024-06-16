import re
import logging
import requests
import pandas as pd
from pprint import pprint
# from send_email import send_email

# from dotenv import load_dotenv
from app_utils import *
from classes import NewsFeed, EmailService


# Configure the logging format and level (DEBUG level is typically used for detailed diagnostic information, good for for developers or system administrators to troubleshoot issues)
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s - %(levelname)s - %(message)s (%(module)s:%(filename)s:%(lineno)d)', level=logging.DEBUG)


# # Load environment variables from the .env file
# load_dotenv()

download_word_list()

def main():
    # Read the contacts file into a DataFrame
    contacts_df = pd.read_excel(CONTACT_FILE)

    # Iterate through each row in the DataFrame
    for _, row in contacts_df.iterrows():
        interest = row['interest']
        receiver = row['email']

        email_body = NewsFeed(interest).download_news()

        EmailService(receiver=receiver,
            subject=f"Your Daily {row['interest']} Digest: Stay Updated!",
            body=email_body).send()

# Check if the script is being run as the main program
if __name__ == "__main__":

    # topic = validate_topic(
    #     "\n\n>> Enter a topic you want to get news about:  ")

    # lang = validate_language(
    #     "\n\n>> Enter a language code in ISO format (e.g., 'en' for English):  ")

    # print("\n\n>> Here are your 20 articles:\n")

    # print(NewsFeed("sex").download_news())

    # email_body = NewsFeed("sex").download_news()

    # EmailService(receiver="dofef22481@morxin.com",
    #              subject="Greeting",
    #              body=email_body).send()

    # df = pd.read_excel(CONTACT_FILE)

    # for _, row in df.iterrows():
    #     interest = row['interest']
    #     receiver = row['email']

    #     email_body = NewsFeed(interest).download_news()

    #     EmailService(receiver=receiver,
    #         subject=f"Your Daily {row['interest']} Digest: Stay Updated!",
    #         body=email_body).send()

    main()