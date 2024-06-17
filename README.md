# NewsWire

## Overview
NewsWire is a Python Command-Line Interface (CLI) application based on Object-Oriented Programming (OOP) principles. It sends personalized news alerts via email to recipients based on their specified interests. The application keeps running and performs the task weekly every Monday at 10:00 AM, broadcasting emails with 10 news articles about each topic/interest during the passing week.

## Features
- **Email News Alerts**: Sends personalized email news alerts to recipients based on their specified interests.
- **Customizable Interests**: Allows users to specify their interests, and the system fetches news articles accordingly.
- **Scheduled Task**: Automatically sends email alerts on a weekly basis every Monday at 10 AM.
- **Continuous Operation**: The application keeps running to ensure timely execution of scheduled tasks.
- **Scalable Contact Management**: Users are free to expand the `contacts.xlsx` file to add contacts with emails and interests, and the app will broadcast emails with 10 news articles about each topic/interest during the passing week.
- **Logging**: Utilizes logging to record detailed information about the application's execution, including errors, warnings, and informational messages.

## News API
The application utilizes the [News API](https://newsapi.org) to fetch news articles based on specified interests.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure the necessary parameters such as API keys and email credentials in `config.py`.
   - Set up environment variables for `NEWS_API_KEY`, `SENDER`, and `PASSWORD`.
5. Prepare a list of contacts with their names, email addresses, interests, and preferred languages in an Excel file and save it as `contacts.xlsx` in the `resources` directory.
6. Run the script using `python main.py`.

## Usage
1. Run the script using `python main.py`.
2. The script will automatically send personalized email news alerts to the recipients listed in the `contacts.xlsx` file at 10:00 AM every Monday.
3. Ensure that the email credentials provided in the `config.py` file are valid and have permission to send emails.

**Note:** During development, disposable email addresses from online services were used for testing purposes.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.