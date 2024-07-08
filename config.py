import os
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Define the time at which you want the task to run
SCHEDULE_TIME = "10:00"

ASSETS = Path(__file__).parent / "assets"
LOGS = ASSETS / "log"
RESOURCES = ASSETS / "resources"
LOG_FILE = LOGS / "app.log"
TOPIC_FILE = RESOURCES / "topics.txt"
CONTACT_FILE = RESOURCES / "contacts.xlsx"

# Define the endpoint and API key for the News API, and the topic we want to search for news
NEWS_API_ENDOINT_EVERYTHING = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
DEFAULT_LANGUAGE = "en"

# Email service config data
SENDER = os.getenv("SENDER")
PASSWORD = os.getenv("PASSWORD")

# Email signature
SIGNATURE = """
Stay tuned for more updates, and have a great day!

Best regards,
Emads
E>
"""

ASCII_ART = """

███╗   ██╗███████╗██╗    ██╗███████╗██╗    ██╗██╗██████╗ ███████╗
████╗  ██║██╔════╝██║    ██║██╔════╝██║    ██║██║██╔══██╗██╔════╝
██╔██╗ ██║█████╗  ██║ █╗ ██║███████╗██║ █╗ ██║██║██████╔╝█████╗  
██║╚██╗██║██╔══╝  ██║███╗██║╚════██║██║███╗██║██║██╔══██╗██╔══╝  
██║ ╚████║███████╗╚███╔███╔╝███████║╚███╔███╔╝██║██║  ██║███████╗
╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚══════╝
                                                                 
"""