#existed_mailbox_connect.py

import pytest
from basic_commands.mailbox_page import MailboxPage
from dashboard_mailboxes.mailbox_credentials import EXISTED_CREDENTIALS

class ExistedMailbox(MailboxPage):
    #@pytest.mark.existed
    def connect_mailbox_existed(self):
        mailbox_page = MailboxPage(self.driver, self.driver.current_url)
        # Connect gmail mailbox
        mailbox_page.select_provider(EXISTED_CREDENTIALS["index"])
        mailbox_page.enter_mailbox_email(EXISTED_CREDENTIALS['email'])
        mailbox_page.enter_mailbox_password(EXISTED_CREDENTIALS['password'])
        mailbox_page.attach_mailbox()
        # Check mailbox connection
        assert mailbox_page.is_connect_existed_failed(), \
            f"Mailbox {EXISTED_CREDENTIALS['email']} should not be connected"
        mailbox_page.move_to_mailbox(EXISTED_CREDENTIALS['email'])
        assert mailbox_page.is_connect_success(EXISTED_CREDENTIALS['email']), \
            f"Mailbox {EXISTED_CREDENTIALS['email']} should be connected"
