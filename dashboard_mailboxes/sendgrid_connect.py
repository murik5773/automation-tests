#sendgrid_connect.py

import pytest
from pages.login_page import LoginPage
from pages.mailbox_page import MailboxPage
from config.settings import USER_CREDENTIALS
from dashboard_mailboxes.mailbox_credentials import SENDGRID_CREDENTIALS

class SendgridConnect(MailboxPage):

    def connect_mailbox(self, email, smtp_password):
        mailbox_page = MailboxPage(self.driver, self.driver.current_url)

        # Connect gmail mailbox
        mailbox_page.select_provider(SENDGRID_CREDENTIALS["index"])
        mailbox_page.enter_mailbox_email(email)
        mailbox_page.enter_send_from_name()
        mailbox_page.enter_smtp_username(smtp_username)
        mailbox_page.enter_smtp_password(smtp_password)
        mailbox_page.enter_smtp_host(smtp_host)
        mailbox_page.enter_smtp_port(smtp_port)
        mailbox_page.enter_imap_username(imap_username)
        mailbox_page.enter_imap_password(imap_password)
        mailbox_page.enter_imap_host(imap_host)
        mailbox_page.enter_imap_port(imap_port)
        mailbox_page.attach_mailbox()
        # Check mailbox connection
        if email == SENDGRID_CREDENTIALS['valid']['email'] and smtp_password == SENDGRID_CREDENTIALS['valid']['smtp_password']:
            assert mailbox_page.is_connect_success(email), f"Mailbox {email} should be connected"
            # Disconnect gmail mailbox
            mailbox_page.disconnect_mailbox()
            # Check mailbox disconnection
            assert mailbox_page.is_disconnect_success(email), f"Mailbox {email} should be disconnected"
        else:
            assert mailbox_page.is_connect_failed(), f"Mailbox {email} should not be connected"