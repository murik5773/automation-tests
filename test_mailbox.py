#test_mailbox.py

import pytest
from basic_commands.login_page import LoginPage
from dashboard_mailboxes.existed_mailbox_connect import ExistedMailbox
from dashboard_mailboxes.gmail_connect import GmailConnect
from dashboard_mailboxes.zoho_connect import ZohoConnect
from dashboard_mailboxes.zoho_pro_connect import ZohoProConnect
from dashboard_mailboxes.yahoo_connect import YahooConnect
from dashboard_mailboxes.aol_connect import AolConnect
from dashboard_mailboxes.sendgrid_connect import SendgridConnect
from config.settings import USER_CREDENTIALS
from dashboard_mailboxes.mailbox_credentials import (
    GMAIL_CREDENTIALS, ZOHO_CREDENTIALS, ZOHO_PRO_CREDENTIALS,
    YAHOO_CREDENTIALS, AOL_CREDENTIALS, SENDGRID_CREDENTIALS, EXISTED_CREDENTIALS
)

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
    # User authorization before mailbox connection
    login_page = LoginPage(driver, driver.current_url)
    login_page.go_to_site()
    login_page.enter_email(USER_CREDENTIALS['valid']['email'])
    login_page.enter_password(USER_CREDENTIALS['valid']['password'])
    login_page.click_login_button()
    assert login_page.is_logged_in(), "User is not logged in"

@pytest.mark.parametrize("credentials", [
    GMAIL_CREDENTIALS,
    # ZOHO_CREDENTIALS,
    # ZOHO_PRO_CREDENTIALS,
    # YAHOO_CREDENTIALS,
    # AOL_CREDENTIALS,
    SENDGRID_CREDENTIALS,
])

@pytest.mark.valid
def test_success_connect_mailbox(driver, login, credentials):
    # Identify the class based on the provider
    connector_class = PROVIDER_CLASS_MAP[credentials['provider']]
    connector = connector_class(driver, driver.current_url)
    connector.connect_mailbox_success()

@pytest.mark.parametrize("credentials", [
    GMAIL_CREDENTIALS,
    # ZOHO_CREDENTIALS,
    # ZOHO_PRO_CREDENTIALS,
    # YAHOO_CREDENTIALS,
    # AOL_CREDENTIALS,
    SENDGRID_CREDENTIALS,
])

@pytest.mark.invalid
def test_failed_connect_mailbox(driver, login, credentials):
    # Identify the class based on the provider
    connector_class = PROVIDER_CLASS_MAP[credentials['provider']]
    connector = connector_class(driver, driver.current_url)
    connector.connect_mailbox_failed()
