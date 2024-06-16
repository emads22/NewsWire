import re
import logging
import requests
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

# Check if the script is being run as the main program
if __name__ == "__main__":

    # topic = validate_topic(
    #     "\n\n>> Enter a topic you want to get news about:  ")

    # lang = validate_language(
    #     "\n\n>> Enter a language code in ISO format (e.g., 'en' for English):  ")

    # print("\n\n>> Here are your 20 articles:\n")

    # print(NewsFeed("sex").download_news())

    email_body = NewsFeed("sex").download_news()

    EmailService(receiver="dofef22481@morxin.com",
                 subject="Greeting",
                 body=email_body).send()
