import re
import logging
import requests
from pprint import pprint
# from send_email import send_email

# from dotenv import load_dotenv
from app_utils import *


# Configure the logging format and level (DEBUG level is typically used for detailed diagnostic information, good for for developers or system administrators to troubleshoot issues)
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s - %(levelname)s - %(message)s (%(module)s:%(filename)s:%(lineno)d)', level=logging.DEBUG)


# # Load environment variables from the .env file
# load_dotenv()

download_word_list()


def main(topic=None, language=None):

    while True:
        # Prompt user to enter receiver email
        receiver = input("\n--- Please enter a receiver email:  ").strip()

        if re.match(EMAIL_PATTERN, receiver):
            # If entered email format is valid, exit loop
            break
        else:
            # If email format is invalid, display error message and prompt user to try again
            print("\n--- Invalid email format. Please try again. ---")

    # Make a GET request to the News API to fetch news articles related to the specified topic with parameters ('q' , 'language', and 'apiKey')
    try:
        response = requests.get(f"{NEWS_API_ENDOINT_EVERYTHING}?q={
                                topic}&language={language}&apiKey={NEWS_API_KEY}")
        response.raise_for_status()  # Raise an HTTPError for bad response status codes
    except requests.exceptions.RequestException as e:
        sys.exit(f"\n--- Failed to fetch news articles: {e} ---\n")

    # Using `request.json()` is better to access data using familiar Python syntax, such as dictionary keys and list indices than using `request.text` which is a plain string (str type)
    content = response.json()

    # Check if the response contains valid data
    if 'articles' not in content:
        sys.exit(
            "\n--- No articles found for the provided topic/language. Please try again. ---\n")

    # define the text block of all articles to be sent by email and total number of articles
    all_articles_data = ""

    # Use Debugging mode to monitor data variables and how they are structures (specially lists and dicts) so we know articles are stored in dict content of key 'articles' and same thing for 'title' and 'description'
    # use the get() with dict to avoid raising an error if key not found, so the default value here returned is [] and slicing on [] returns []
    # Limit to the first 20 articles
    for article in content.get('articles', [])[:20]:
        # here no need to define default value wth get() cz if key not found None returned and below the condition filters articles with None data
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')

        # Check if necessary data is available
        if title and description and url:
            # Add all three article data to text block by concatenation
            all_articles_data += f"{title}:\n{description}\n{url}\n\n"

    # check if the text block isnt empty in order to send it by email
    if all_articles_data.strip():
        # send an email of all these articles text block and handle the outcome
        subject = f"{topic.title()} News: The Latest Updates and Headlines"
        if send_email(all_articles_data, subject, receiver):
            sys.exit(f'\n\n--- "{topic.title()
                                 }" news emailed successfully. ---\n\n')
        else:
            sys.exit("\n\n--- Failed to send email. Please try again later ---\n\n")
    else:
        sys.exit(
            "\n\n--- No articles found for the provided topic. Please try again. ---\n\n")


# Check if the script is being run as the main program
if __name__ == "__main__":

    topic = validate_topic(
        "\n\n>> Enter a topic you want to get news about:  ")

    lang = validate_language(
        "\n\n>> Enter a language code in ISO format (e.g., 'en' for English):  ")

    print("\n\n>> Here are your 20 articles:\n")

    all_articles = fetch_articles(topic, lang)

    articles_cleaned = [dict(title=article['title'], description=article['description']) for article in all_articles if article.get('title') and article.get('description')]

    pprint(articles_cleaned, sort_dicts=False)