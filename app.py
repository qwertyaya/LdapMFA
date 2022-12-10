import os
import random
import string
import telebot
import ldap3
from rich import print
from dotenv import load_dotenv
from rich.console import Console
from ldap3 import Server, Connection, ALL

# Constants

load_dotenv()
TOKEN = os.environ.get("TOKEN")
TG_UID = input(
    'Enter Your Telegram ID \n You can find your id by looking for "userinfobot" pn Telegram \n>>>')
PASS = 0

console = Console()

# Approved users, username: telegram_id
aproved_users = {
    os.environ.get("username"): TG_UID,  # Value: Telegram UID (int)
}


def check_credentials(url: str, username: str) -> bool:
    """
    check_credentials

    Args:
        url ([str]): [LDAP server url]
        username ([str]): [Username]
    """
    server = Server(url)
    """ 
    To be able to connect as administrator to openldap
    """
    with Connection(server, f'cn=admin,dc=example,dc=org', os.environ.get("adminpassword")) as conn:
        user_data = {}
        entries = conn.extend.standard.paged_search(
            'dc=example,dc=org', '(objectClass=person)', attributes=['cn', 'givenName'], paged_size=5)
        for entry in entries:
            user_data['user'] = entry
            q = str(user_data['user']['dn'])
            if username in q:
                return True


def telegram_bot(api_token: str):
    """
    Function to create a bot, generate random code and send it to the user
    Args:
        api_token ([str]): [TG Bot Api Token]
    """
    global PASS
    bot = telebot.TeleBot(api_token)
    PASS = int(generate_random_code())
    bot.send_message(search_in_dict(aproved_users, username), PASS)


def search_in_dict(dct: dict, key: str) -> int:
    """
    Search a user in a dict and return the his TG UID
    Args:
        dct ([dict]): [dictionary of users]
        key ([str]): [username]
    Returns:
        [type]: [description]
    """
    for k, v in dct.items():
        if k == key:
            return v


def generate_random_code() -> str:
    """
    Generate a random MFA code
    Returns:
        [int]: [random code]
    """
    return ''.join(random.choice(string.digits) for _ in range(6))


def connect_to_ldap(username: str, password: str, ldap_url: str):
    """
    Check if the given username and password exists in OpenLDAP.
    Args:
        username (str): The username to check.
        password (str): The password to check.
        ldap_url (str): The URL of the OpenLDAP server.
        ldap_domain (str): The LDAP domain of the OpenLDAP server.
    Returns:
        bool: True if the username and password exists, False otherwise.
    """
    # define the server
    # define an unsecure LDAP server, requesting info on DSE and schema
    s = Server(ldap_url, get_info=ALL)

    # define the connection
    try:
        c = Connection(s, user=username, password=password)
        print('connected')
    except Exception as e:
        if not c.bind():
            print('error in bind', c.result)


if __name__ == '__main__':
    url = input('Enter LDAP URL (localhost:port): \n>>> ')
    username = input('Enter username (username): \n>>> ')
    password = input('Enter password (password): \n>>> ')

    if check_credentials(url, username):
        try:
            telegram_bot(TOKEN)
            code = int(input('Enter the authentication code from bot:\n'))
            if code == PASS:
                connect_to_ldap(username, password, url)
                console.print(f'{username} is logged in!')
            else:
                console.print('Wrong code!')
        except Exception as e:
            print('q')
            print(e)
