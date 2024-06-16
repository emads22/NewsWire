import logging
import requests
import time
import schedule
from datetime import datetime
import pandas as pd
from app_utils import download_word_list
from classes import NewsFeed, EmailService
from config import LOG_FILE


# Configure the logging format and level (DEBUG level is typically used for detailed diagnostic information, good for for developers or system administrators to troubleshoot issues)
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s - %(levelname)s - %(message)s (%(module)s:%(filename)s:%(lineno)d)', level=logging.DEBUG)


download_word_list()

# schedule.every().day.at("20:32").do(lambda: print("emads"))
schedule.every().day.at("20:32").do(lambda: main())


def main():
    # Read the contacts file into a DataFrame
    contacts_df = pd.read_excel(CONTACT_FILE)

    # Iterate through each row in the DataFrame
    for _, row in contacts_df.iterrows():
        interest = row['interest']
        receiver = row['email']

        email_body = NewsFeed(interest).download_news()

        EmailService(receiver=receiver,
                     subject=f'Your "{interest}" News Alert: Stay Connected!',
                     body=email_body).send()


# Check if the script is being run as the main program
if __name__ == "__main__":

    # # METHOD 1:
    # while True:

    #     # Periodically every 1 minute check to run program on specific time
    #     now = datetime.now()  # Capture the current time once

    #     if now.hour == 20 and now.minute == 24:
    #         main()
    #         # print("emads")

    #     time.sleep(60)

    # METHOD 2:
    while True:

        schedule.run_pending()

        time.sleep(60)




        

    # topic = validate_topic(
    #     "\n\n>> Enter a topic you want to get news about:  ")

    # lang = validate_language(
    #     "\n\n>> Enter a language code in ISO format (e.g., 'en' for English):  ")

    # print("\n\n>> Here are your 20 articles:\n")

    # print(NewsFeed("tesla").download_news())

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
