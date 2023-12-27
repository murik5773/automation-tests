#sendgrid_connect.py

import pytest
from basic_commands.mailbox_page import MailboxPage
from dashboard_mailboxes.mailbox_credentials import SENDGRID_CREDENTIALS

class SendgridConnect(MailboxPage):

    def __init__(self, driver, current_url):
        self.mailbox_page = MailboxPage(driver, driver.current_url)

    def connect_mailbox_success(self):
        # Connect gmail mailbox
        self.mailbox_page.select_provider(SENDGRID_CREDENTIALS["index"])
        self.mailbox_page.enter_mailbox_email(SENDGRID_CREDENTIALS['valid']['email'])
        self.mailbox_page.enter_send_from_name()
        self.mailbox_page.select_tariff_plan()
        self.mailbox_page.enter_smtp_username(SENDGRID_CREDENTIALS['valid']['smtp_username'])
        self.mailbox_page.enter_smtp_password(SENDGRID_CREDENTIALS['valid']['smtp_password'])
        self.mailbox_page.enter_smtp_host(SENDGRID_CREDENTIALS['valid']['smtp_host'])
        self.mailbox_page.enter_smtp_port(SENDGRID_CREDENTIALS['valid']['smtp_port'])
        #self.mailbox_page.enter_imap_username(SENDGRID_CREDENTIALS['valid']['imap_username'])
        self.mailbox_page.enter_imap_password(SENDGRID_CREDENTIALS['valid']['imap_password'])
        self.mailbox_page.enter_imap_host(SENDGRID_CREDENTIALS['valid']['imap_host'])
        self.mailbox_page.enter_imap_port(SENDGRID_CREDENTIALS['valid']['imap_port'])
        self.mailbox_page.attach_mailbox()
        # Check mailbox connection
        assert self.mailbox_page.is_connect_success(
            SENDGRID_CREDENTIALS['valid']['email']), \
            f"Mailbox {SENDGRID_CREDENTIALS['valid']['email']} should be connected"
        # self.connect_mailbox_existed()
        # Disconnect gmail mailbox
        self.mailbox_page.disconnect_mailbox()
        # Check mailbox disconnection
        assert self.mailbox_page.is_disconnect_success(
            SENDGRID_CREDENTIALS['valid']['email']), \
            f"Mailbox {SENDGRID_CREDENTIALS['valid']['email']} should be disconnected"

    # @pytest.mark.invalid
    def connect_mailbox_failed(self):
        # Connect gmail mailbox
        self.mailbox_page.select_provider(SENDGRID_CREDENTIALS["index"])
        self.mailbox_page.enter_mailbox_email(SENDGRID_CREDENTIALS['valid']['email'])
        self.mailbox_page.enter_send_from_name()
        self.mailbox_page.enter_smtp_username(SENDGRID_CREDENTIALS['valid']['smtp_username'])
        self.mailbox_page.enter_smtp_password(SENDGRID_CREDENTIALS['valid']['smtp_password'])
        self.mailbox_page.enter_smtp_host(SENDGRID_CREDENTIALS['valid']['smtp_host'])
        self.mailbox_page.enter_smtp_port(SENDGRID_CREDENTIALS['valid']['smtp_port'])
        # self.mailbox_page.enter_imap_username(SENDGRID_CREDENTIALS['valid']['imap_username'])
        self.mailbox_page.enter_imap_password(SENDGRID_CREDENTIALS['invalid']['imap_password'])
        self.mailbox_page.enter_imap_host(SENDGRID_CREDENTIALS['valid']['imap_host'])
        self.mailbox_page.enter_imap_port(SENDGRID_CREDENTIALS['valid']['imap_port'])
        # self.mailbox_page.attach_mailbox()
        # assert self.mailbox_page.is_connect_without_tariff_failed(), \
        #    f"Mailbox {GMAIL_CREDENTIALS['valid']['email']} should not be connected"
        self.mailbox_page.select_tariff_plan()
        # self.mailbox_page.enter_mailbox_email(GMAIL_CREDENTIALS['valid']['email'])
        # self.mailbox_page.enter_mailbox_password(GMAIL_CREDENTIALS['invalid']['password'])
        self.mailbox_page.attach_mailbox()
        # Check mailbox connection
        assert self.mailbox_page.is_connect_invalid_failed(), \
            f"Mailbox {SENDGRID_CREDENTIALS['valid']['email']} should not be connected"
        self.mailbox_page.enter_smtp_password(SENDGRID_CREDENTIALS['invalid']['smtp_password'])
        self.mailbox_page.enter_imap_password(SENDGRID_CREDENTIALS['valid']['imap_password'])
        self.mailbox_page.attach_mailbox()
        # Check mailbox connection
        assert self.mailbox_page.is_connect_invalid_failed(), \
            f"Mailbox {SENDGRID_CREDENTIALS['invalid']['email']} should not be connected"