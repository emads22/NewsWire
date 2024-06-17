import logging
import nltk
import pycountry
from nltk.corpus import words
from nltk.data import find
from config import *


def download_word_list():
    """
    Downloads the NLTK word list if it is not already downloaded.

    This function checks if the NLTK word list is available locally.
    If not, it downloads the word list using NLTK's download function.
    """
    try:
        # Check if the NLTK word list is available
        find('corpora/words.zip')
    except LookupError:
        # If the word list is not found, log a warning and download it
        logging.warning("NLTK word list not found. Initiating download.")
        nltk.download('words')


def format_email_body(recipient, topic, text_body=None):
    """
    Formats the email body with recipient's name, topic, and text body.

    Args:
        text_body (str): The body text containing news article titles and URLs.
        recipient (str): The name of the email recipient.
        topic (str): The topic or interest of the news articles.

    Returns:
        str: The formatted email body.
    """

    formatted_body = f"""
Hi {recipient},


We hope this email finds you well.
"""

    if text_body is None:
        formatted_body += f"""
Sorry, no news articles available for "{topic}" this week.
"""

    else:
        formatted_body += f"""
Here are the latest "{topic}" news articles to keep you informed:

{text_body}
"""

    formatted_body += SIGNATURE

    return formatted_body


def load_topics():
    """
    Loads topics from an external file.

    This function reads topics from a predefined file and returns them as a list.
    If the file cannot be read, it logs a warning and returns an empty list.

    Returns:
        list: A list of topics loaded from the file.
    """
    topics = []

    try:
        # Open the topic file and read each line, stripping any extra whitespace
        with open(TOPIC_FILE) as f:
            topics = [line.strip() for line in f.readlines()]
    except Exception as e:
        # Log a warning if there's an issue reading the file
        logging.warning(f"Failure in loading topics from external file: {e}")

    return topics


def validate_topic(prompt):
    """
    Prompts the user to input a valid topic.

    This function repeatedly prompts the user for a topic until a valid one is entered.
    A valid topic is one that is either in the predefined STOCKS list or
    in the combined list of loaded topics and NLTK words.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        str: A valid topic entered by the user.
    """
    while True:
        try:
            # Prompt the user for a topic and convert it to lowercase
            topic = input(prompt).strip().lower()
            word_list = words.words()  # Load the NLTK word list
            topic_list = load_topics()  # Load the topics from the external file

            # Validate the topic
            if topic.upper() not in STOCKS and topic not in (topic_list + word_list):
                raise ValueError

            return topic

        except ValueError:
            # Print an error message if the topic is not valid
            print("\n\n-- Please enter a meaningful topic. For example: 'tesla', 'sports', 'politics', 'bitcoin', etc. --")


def validate_language(prompt):
    """
    Prompts the user to input a valid language code in ISO format.

    This function repeatedly prompts the user for a language code until a valid one is entered.
    A valid language code is one that exists in the list of ISO 639-1 language codes.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        str: A valid language code entered by the user.
    """
    while True:
        try:
            # Prompt the user for a language code and convert it to lowercase
            lang_input = input(prompt).strip().lower()
            lang_iso_list = [language.alpha_2 for language in pycountry.languages if hasattr(
                language, 'alpha_2')]

            # Validate the language code
            if lang_input not in lang_iso_list:
                raise ValueError

            return lang_input

        except ValueError:
            # Print an error message if the language code is not valid
            print(
                "\n\n-- Please enter a language code in ISO format (e.g., 'en' for English). --")
