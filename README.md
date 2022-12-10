# LdapMFA
The LDAP Login Script is a Python script that allows users to log in to an LDAP server using their username and password. It also includes a Telegram bot that sends the user a one-time password (OTP) for additional authentication.
Requirements
The LDAP Login Script requires the following libraries:

ldap3
rich
telebot
To install these libraries, run the following command:


pip install ldap3 rich telebot
Usage
To use the LDAP Login Script, run the python ldap_login.py command and follow the prompts to enter the LDAP server URL, your username, and password. The script will then send you an OTP via a Telegram bot, which you need to enter to complete the authentication process.


python ldap_login.py
Enter LDAP URL (ldap.forumsys.com):
>>> ldap://ldap.forumsys.com:389/
Enter username (read-only-admin):
>>> read-only-admin
Enter password (password):
>>> password
Configuration
The LDAP Login Script uses the following environment variables:

TG_BOT_TOKEN: The API token of the Telegram bot that sends the OTP.
TG_UID: The user ID of the Telegram user who will receive the OTP.
To set these environment variables, create a .env file in the same directory as the script and add the following lines:


TG_BOT_TOKEN=your_bot_token
TG_UID=your_user_id
Contributing
If you want to contribute to the LDAP Login Script, please follow these guidelines:

Fork the repository and create a new branch for your changes.
Make your changes and add tests to cover them.
Run the tests to ensure they pass.
Submit a pull request to the master branch of the main repository.
License
The LDAP Login Script is licensed under the MIT License. See the LICENSE file for more details.
