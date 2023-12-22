#zoho_pro_connect.py

import pytest
from pages.login_page import LoginPage
from pages.mailbox_page import MailboxPage
from config.settings import USER_CREDENTIALS
from dashboard_mailboxes.mailbox_credentials import ZOHO_PRO_CREDENTIALS

class ZohoProConnect(MailboxPage):

    def connect_mailbox(self, email, password):
        mailbox_page = MailboxPage(self.driver, self.driver.current_url)

        # Connect gmail mailbox
        mailbox_page.select_provider(ZOHO_PRO_CREDENTIALS["index"])
        mailbox_page.enter_mailbox_email(email)
        mailbox_page.enter_mailbox_password(password)
        mailbox_page.enter_send_from_name()
        mailbox_page.attach_mailbox()
        # Check mailbox connection
        assert mailbox_page.is_connect_success(email), f"Mailbox {email} should be connected"

        # Disconnect a new mailbox
        mailbox_page.disconnect_mailbox()
        # Check mailbox disconnection
        if email == ZOHO_PRO_CREDENTIALS['valid']['email'] and password == ZOHO_PRO_CREDENTIALS['valid']['password']:
            assert mailbox_page.is_connect_success(email), f"Mailbox {email} should be connected"
            # Disconnect gmail mailbox
            mailbox_page.disconnect_mailbox()
            # Check mailbox disconnection
            assert mailbox_page.is_disconnect_success(email), f"Mailbox {email} should be disconnected"
        else:
            assert mailbox_page.is_connect_failed(), f"Mailbox {email} should not be connected"