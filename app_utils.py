import os
import logging
import requests
import nltk
import pycountry
from nltk.corpus import words
from nltk.data import find
from datetime import datetime, timedelta
import pandas as pd
from config import *


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


def build_news_url(topic, language, apikey=os.getenv("NEWS_API_KEY")):

    today = datetime.now()
    yesterday = today - timedelta(days=30)

    url = f"{NEWS_API_ENDOINT_EVERYTHING}?q={topic}&from={
        today.isoformat()}&to={yesterday.isoformat()}&language={language}&apiKey={apikey}"

    return url


def fetch_articles(topic, language='en', number=20):
    try:
        news_url = build_news_url(topic, language)
        response = requests.get(url=news_url)
        response.raise_for_status()
        content = response.json()
        articles = content.get('articles', [])

        if not articles:
            logging.error(
                "No articles found for the provided topic/language.")
            return articles

        return articles[:number]

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    return []


def extract_news_data(articles):
    if not articles:
        return None

    articles_data = "\n"

    for article in articles:
        if article.get('title') and article.get('url'):
            articles_data += f"""
> {article['title']}
  {article['url']}
"""
    articles_data += "\n"

    return articles_data


def extract_excel_data(filepath):
    df = pd.read_excel(filepath)
    for _, row in df.iterrows():
        print(row['interest'])



if __name__ == "__main__":
    print(extract_excel_data(CONTACT_FILE))
