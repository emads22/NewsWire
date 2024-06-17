import logging
import time
import schedule
import sys
import pandas as pd
from datetime import datetime
from app_utils import download_word_list, format_email_body
from newsfeed import NewsFeed
from email_service import EmailService
from config import SCHEDULE_TIME, LOG_FILE, CONTACT_FILE

# Configure the logging format and level (DEBUG level is typically used for detailed diagnostic information, good for troubleshooting issues)
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s - %(levelname)s - %(message)s (%(module)s:%(filename)s:%(lineno)d)',
                    level=logging.DEBUG)

# Download the NLTK word list if it is not already downloaded
download_word_list()

# Schedule the task to run weekly on the specified day and time
schedule.every().monday.at(SCHEDULE_TIME).do(lambda: main())


def main():
    try:
        # Read the contacts file into a DataFrame
        contacts_df = pd.read_excel(CONTACT_FILE)

        # Iterate through each row in the DataFrame
        for _, row in contacts_df.iterrows():
            name = row['Name']
            receiver = row['Email']
            interest = row['Interest']
            language = row['Language']

            # Fetch news articles based on the interest and prepare the email body
            news_feed = NewsFeed(interest, language).download_news()

            if news_feed is None:
                email_body = format_email_body(recipient=name, topic=interest)

            else:
                email_body = format_email_body(
                    text_body=news_feed, recipient=name, topic=interest)

            # Send the email to the recipient
            EmailService(receiver=receiver,
                         subject=f'Your "{
                             interest}" News Alert: Stay Connected!',
                         body=email_body).send()

        logging.info(f"Emails sent successfully to all recipients on {
            datetime.now().strftime('%Y-%m-%d')}.")
        print(f"\n\n--- Emails sent successfully to all recipients on {
            datetime.now().strftime('%Y-%m-%d')}. ---\n\n")

    except Exception as e:
        # Log any exceptions that occur during the execution of the main function
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)
        sys.exit(
            "\n\n--- An unexpected error occurred. The application will now exit. Please check the logs for more details. ---\n\n")


if __name__ == "__main__":
    # Run the scheduling loop to check for scheduled tasks
    while True:
        schedule.run_pending()  # Run any pending scheduled tasks
        time.sleep(60)  # Sleep for 1 hour before checking again
