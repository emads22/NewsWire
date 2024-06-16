import logging
import re
import nltk
import pycountry
from nltk.corpus import words
from nltk.data import find
from constants import TOPIC_PATTERN, TOPIC_FILE, STOCKS


def download_word_list():
    """
    Downloads the NLTK word list if it is not already downloaded.
    """
    try:
        find('corpora/words.zip')
    except LookupError:
        logging.warning(
            f"NLTK word list is not already downloaded. Proceed to download it.")
        nltk.download('words')


def load_topics():
    topics = []

    try:
        with open(TOPIC_FILE) as f:
            topics = [line.strip() for line in f.readlines()]
    except Exception as e:
        logging.warning(f"Failure in loading topics from external file: {e}")

    return topics


def validate_topic(prompt):

    while True:
        try:
            topic = input(prompt).strip().lower()
            word_list = words.words()
            topic_list = load_topics()

            # validate the topic
            if topic.upper() not in STOCKS and topic not in topic_list + word_list:
                raise ValueError

            return topic

        except ValueError:
            # Print an error message if the topic is not valid
            print("\n\n-- Please enter a meaningful topic. For example: 'tesla', 'sports', 'politics', 'bitcoin', etc. --")


def validate_language(prompt):
    while True:
        try:
            lang_input = input(prompt).strip().lower()
            lang_iso_list = [language.alpha_2 for language in pycountry.languages if hasattr(
                language, 'alpha_2')]

            # validate the topic
            if lang_input not in lang_iso_list:
                raise ValueError

            return lang_input

        except ValueError:
            # Print an error message if the topic is not valid
            print(
                "\n\n-- Please enter a language code in ISO format (e.g., 'en' for English). --")
