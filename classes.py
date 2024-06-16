import os
import logging
import requests
import nltk
import pycountry
from nltk.corpus import words
from nltk.data import find
from datetime import datetime, timedelta
from constants import *


class NewsFeed:
    """
    A class to fetch news articles from the News API based on specified criteria.

    Attributes:
        base_url (str): The base URL for the News API.
        api_key (str): The API key for accessing the News API.
        interest (str): The interest for which news articles are fetched.
        language (str): The language of the news articles (default is 'en').
        from_date (datetime): The start date for fetching articles.
        to_date (datetime): The end date for fetching articles.
        max_articles (int): The maximum number of articles to fetch (default is 20).
    """

    base_url = "NEWS_API_ENDOINT_EVERYTHING"
    # Get the API key from environment variables
    api_key = os.getenv("NEWS_API_KEY")

    def __init__(self,
                 interest: str,
                 language: str = 'en',
                 from_date: datetime = datetime.now() - timedelta(days=30),
                 to_date: datetime = datetime.now(),
                 max_articles: int = 20) -> None:
        """
        Initializes a NewsFeed object with the specified parameters.

        Args:
            interest (str): The interest for which news articles are fetched.
            language (str, optional): The language of the news articles (default is 'en').
            from_date (datetime, optional): The start date for fetching articles (default is 30 days (1 month) ago).
            to_date (datetime, optional): The end date for fetching articles (default is current date).
            max_articles (int, optional): The maximum number of articles to fetch (default is 20).
        """
        self.interest = interest
        self.language = language
        self.from_date = from_date.isoformat()
        self.to_date = to_date.isoformat()
        self.max_articles = max_articles

    def build_news_api_url(self) -> str:
        """
        Builds the URL for fetching news articles from the News API.

        Returns:
            str: The constructed URL for fetching news articles.
        """
        url = f"{self.base_url}?q={self.interest}&from={self.from_date}&to={
            self.to_date}&language={self.language}&apiKey={self.api_key}"
        return url

    def fetch_news_articles(self) -> list:
        """
        Fetches news articles from the News API.

        Returns:
            list: A list of dictionaries containing news article data.
        """
        try:
            news_url = self.build_news_api_url()
            response = requests.get(url=news_url)
            response.raise_for_status()
            content = response.json()
            articles = content.get('articles')

            if not articles:
                logging.error(
                    "No articles found for the provided interest/language.")

            return articles[:self.max_articles]

        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return []
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return []

    def extract_news_data(self) -> str:
        """
        Extracts news article titles and URLs from fetched articles.

        Returns:
            str: A formatted string containing article titles and URLs.
        """
        articles = self.fetch_news_articles()

        if not articles:
            return None

        articles_data = "\n"

        for article in articles:
            title = article.get('title')
            url = article.get('url')
            if title and url:
                articles_data += f"* {title}\n  {url}\n\n"

        return articles_data

    def download_news(self) -> str:
        """
        Downloads news articles and returns them as a formatted string.

        Returns:
            str: A formatted string containing downloaded news articles.
        """
        return self.extract_news_data()
