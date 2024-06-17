from config import *


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
