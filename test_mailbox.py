#test_mailbox.py

import pytest
from pages.login_page import LoginPage
from pages.mailbox_page import MailboxPage
from dashboard_mailboxes.gmail_connect import GmailConnect
from dashboard_mailboxes.zoho_connect import ZohoConnect
from dashboard_mailboxes.zoho_pro_connect import ZohoProConnect
from dashboard_mailboxes.yahoo_connect import YahooConnect
from dashboard_mailboxes.aol_connect import AolConnect
from dashboard_mailboxes.sendgrid_connect import SendgridConnect
from config.settings import USER_CREDENTIALS, BASE_URL
from dashboard_mailboxes.mailbox_credentials import GMAIL_CREDENTIALS, ZOHO_CREDENTIALS, ZOHO_PRO_CREDENTIALS, YAHOO_CREDENTIALS, AOL_CREDENTIALS, SENDGRID_CREDENTIALS

PROVIDER_CLASS_MAP = {
    "gmail": GmailConnect,
    "zoho": ZohoConnect,
    "zoho_pro": ZohoProConnect,
    "yahoo": YahooConnect,
    "aol": AolConnect,
    "sendgrid": SendgridConnect,
}

@pytest.fixture(scope="function")
def login(driver):
    """User authorization before mailbox connection"""
    login_page = LoginPage(driver, driver.current_url)
    login_page.go_to_site()
    login_page.enter_email(USER_CREDENTIALS['valid']['email'])
    login_page.enter_password(USER_CREDENTIALS['valid']['password'])
    login_page.click_login_button()
    assert login_page.is_logged_in()

@pytest.mark.parametrize("credentials", [
    (GMAIL_CREDENTIALS),
    (ZOHO_CREDENTIALS),
    (ZOHO_PRO_CREDENTIALS),
    (YAHOO_CREDENTIALS),
    (AOL_CREDENTIALS),
    (SENDGRID_CREDENTIALS),
])

def test_connect_mailbox(driver, login, credentials):
    # Identify the class based on the provider
    connector_class = PROVIDER_CLASS_MAP[credentials['provider']]
    connector = connector_class(driver, driver.current_url) # use the base production URL

    # Valid credentials for credentials
    valid_email = credentials['valid']['email']
    valid_password = credentials['valid']['password']

    # Invalid credentials for credentials
    invalid_email = credentials['invalid']['email']
    invalid_password = credentials['invalid']['password']

     # Connect a new mailbox
    connector.connect_mailbox(valid_email, valid_password)