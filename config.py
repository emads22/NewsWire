import os
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


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

SENDER = os.getenv("SENDER")
PASSWORD = os.getenv("PASSWORD")
RECEIVER = os.getenv("RECEIVER")


# Validation patterns
# topic consists of only word characters (letters, digits, and underscores)
TOPIC_PATTERN = r'^\w+$'
# language consists of exactly two lowercase letters
LANGUAGE_PATTERN = r'^[a-z]{2}$'
EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

STOCKS = [
    "AAPL",  # Apple Inc.
    "MSFT",  # Microsoft Corporation
    "AMZN",  # Amazon.com Inc.
    "GOOGL",  # Alphabet Inc. (Google)
    "META",  # Meta Platforms, Inc. (formerly Facebook)
    "TSLA",  # Tesla, Inc.
    "BRK",  # Berkshire Hathaway Inc.
    "TCEHY",  # Tencent Holdings Limited
    "BABA",  # Alibaba Group Holding Limited
    "JNJ",  # Johnson & Johnson
    "JPM",  # JPMorgan Chase & Co.
    "V",  # Visa Inc.
    "MA",  # Mastercard Incorporated
    "WMT",  # Walmart Inc.
    "PG",  # Procter & Gamble Company
    "BAC",  # Bank of America Corporation
    "NSRGY",  # Nestle S.A.
    "005930.KS",  # Samsung Electronics Co., Ltd.
    "DIS",  # Walt Disney Company
    "HD",  # Home Depot, Inc.
    "INTC",  # Intel Corporation
    "TSM",  # Taiwan Semiconductor Manufacturing Company Limited (TSMC)
    "ADBE",  # Adobe Inc.
    "CSCO",  # Cisco Systems, Inc.
    "NKE",  # Nike, Inc.
    "PFE",  # Pfizer Inc.
    "UNH",  # UnitedHealth Group Incorporated
    "MCD",  # McDonald's Corporation
    "VZ",  # Verizon Communications Inc.
    "XOM",  # Exxon Mobil Corporation
    "TM",  # Toyota Motor Corporation
    "IBM",  # IBM (International Business Machines) Corporation
    "KO",  # Coca-Cola Company
    "GE",  # General Electric Company
    "NFLX",  # Netflix, Inc.
    "ABT",  # Abbott Laboratories
    "BA",  # Boeing Company
    "CAT",  # Caterpillar Inc.
    "CVX",  # Chevron Corporation
    "CMCSA",  # Comcast Corporation
    "DHR",  # Danaher Corporation
    "DELL",  # Dell Technologies Inc.
    "LLY",  # Eli Lilly and Company
    "F",  # Ford Motor Company
    "GM",  # General Motors Company
    "GS",  # Goldman Sachs Group, Inc.
    "HON",  # Honeywell International Inc.
    "JCI",  # Johnson Controls International plc
    "LMT",  # Lockheed Martin Corporation
    "MDT",  # Medtronic plc
    "MU",  # Micron Technology, Inc.
    "MS",  # Morgan Stanley
    "ORCL",  # Oracle Corporation
    "PEP",  # PepsiCo, Inc.
    "QCOM",  # Qualcomm Incorporated
    "RTX",  # Raytheon Technologies Corporation
    "CRM",  # Salesforce.com, Inc.
    "SLB",  # Schlumberger Limited
    "SIEGY",  # Siemens AG
    "TXN",  # Texas Instruments Incorporated
    "TTE",  # TotalEnergies SE
    "UPS",  # United Parcel Service, Inc. (UPS)
    "UNP",  # Union Pacific Corporation
    "UTX",  # United Technologies Corporation
    "WFC",  # Wells Fargo & Company
    "AZN",  # AstraZeneca plc
    "BBL",  # BHP Group
    "BMY",  # Bristol-Myers Squibb Company
    "CVS",  # CVS Health Corporation
    "DEO",  # Diageo plc
    "D",  # Dominion Energy, Inc.
    "DUK",  # Duke Energy Corporation
    "GSK",  # GlaxoSmithKline plc
    "MRK",  # Merck & Co., Inc.
    "NEE",  # NextEra Energy, Inc.
    "NVS",  # Novartis AG
    "NVDA",  # NVIDIA Corporation
    "OXY",  # Occidental Petroleum Corporation
    "PM",  # Philip Morris International Inc.
    "RIO",  # Rio Tinto Group
    "RDS",  # Royal Dutch Shell plc
    "SNY",  # Sanofi
    "ARAMCO",  # Saudi Aramco
    "SONY"  # Sony Group Corporation
]
