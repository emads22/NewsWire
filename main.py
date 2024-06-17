import logging
import time
import schedule
import sys
import pandas as pd
from app_utils import download_word_list
from newsfeed import NewsFeed
from email_service import EmailService
from config import LOG_FILE, CONTACT_FILE

# Configure the logging format and level (DEBUG level is typically used for detailed diagnostic information, good for troubleshooting issues)
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s - %(levelname)s - %(message)s (%(module)s:%(filename)s:%(lineno)d)',
                    level=logging.DEBUG)

# Download the NLTK word list if it is not already downloaded
download_word_list()

# Schedule the main function to run every day at 20:32
schedule.every().day.at("20:32").do(lambda: main())


def main():
    try:
        # Read the contacts file into a DataFrame
        contacts_df = pd.read_excel(CONTACT_FILE)

        # Iterate through each row in the DataFrame
        for _, row in contacts_df.iterrows():            
            receiver = row['Email']
            interest = row['Interest']
            language = row['Language']

            # Fetch news articles based on the interest and prepare the email body
            email_body = NewsFeed(interest, language).download_news()

            # Send the email to the recipient
            EmailService(receiver=receiver,
                         subject=f'Your "{
                             interest}" News Alert: Stay Connected!',
                         body=email_body).send()
    except Exception as e:
        # Log any exceptions that occur during the execution of the main function
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)
        sys.exit(
            "\n\nAn unexpected error occurred. The application will now exit. Please check the logs for more details.\n\n")


if __name__ == "__main__":
    # Run the scheduling loop to check for scheduled tasks
    while True:
        schedule.run_pending()  # Run any pending scheduled tasks
        time.sleep(60)  # Sleep for 60 seconds before checking again