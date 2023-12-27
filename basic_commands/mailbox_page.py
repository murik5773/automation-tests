# mailbox_page.py
from basic_commands.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MailboxPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "api_password")
    SEND_FROME_INPUT = (By.ID, "from_name")
    SMTP_USERNAME_INPUT = (By.ID, "smtp_user_name")
    SMTP_PASSWORD_INPUT = (By.ID, "smtp_password")
    SMTP_HOST_INPUT = (By.ID, "smtp_address")
    SMTP_PORT_INPUT = (By.ID, "smtp_port")
    IMAP_USERNAME_INPUT = (By.ID, "imap_user_name")
    IMAP_PASSWORD_INPUT = (By.ID, "imap_password")
    IMAP_HOST_INPUT = (By.ID, "imap_address")
    IMAP_PORT_INPUT = (By.ID, "imap_port")
    CONFIGURE_BUTTON = (By.CLASS_NAME, "tip-block__btn")
    CONNECT_BUTTON = (By.CLASS_NAME, "mailbox-form__btn")
    SUCCESSFUL_CONNECT_MARKER = (By.CLASS_NAME, "mailbox-page__email-name")
    FAILED_CONNECT_MARKER = (By.CLASS_NAME, "regular-feedback__content")
    SUCCESSFUL_DISCONNECT_MARKER = (By.CLASS_NAME, "mailboxes-overview__table")

    def select_provider(self, index):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "navbar__add-mailbox-btn"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mailbox-provider-card")))
        email_providers = self.driver.find_elements(By.CLASS_NAME, "mailbox-provider-card")
        email_providers[index].click()
        connect_instruction = self.wait.until(EC.element_to_be_clickable((self.CONFIGURE_BUTTON)))
        connect_instruction.click()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def enter_mailbox_email(self, email):
        email_input = self.wait.until(EC.presence_of_element_located((self.EMAIL_INPUT)))
        line_length = len(email_input.get_attribute("value"))
        email_input.send_keys("\b" * line_length)
        email_input.send_keys(email)

    def enter_mailbox_password(self, password):
        password_input = self.wait.until(EC.presence_of_element_located((self.PASSWORD_INPUT)))
        line_length = len(password_input.get_attribute("value"))
        password_input.send_keys("\b" * line_length)
        password_input.send_keys(password)

    def enter_send_from_name(self):
        send_from_input = self.wait.until(EC.presence_of_element_located((self.SEND_FROME_INPUT)))
        line_length = len(send_from_input.get_attribute("value"))
        send_from_input.send_keys("\b" * line_length)
        send_from_input.send_keys("Anthony Stark")

    def enter_smtp_username(self, smtp_username):
        smtp_username_input = self.wait.until(EC.presence_of_element_located((self.SMTP_USERNAME_INPUT)))
        line_length = len(smtp_username_input.get_attribute("value"))
        smtp_username_input.send_keys("\b" * line_length)
        smtp_username_input.send_keys(smtp_username)

    def enter_smtp_password(self, smtp_password):
        smtp_password_input = self.wait.until(EC.presence_of_element_located((self.SMTP_PASSWORD_INPUT)))
        line_length = len(smtp_password_input.get_attribute("value"))
        smtp_password_input.send_keys("\b" * line_length)
        smtp_password_input.send_keys(smtp_password)

    def enter_smtp_host(self, smtp_host):
        smtp_host_input = self.wait.until(EC.presence_of_element_located((self.SMTP_HOST_INPUT)))
        line_length = len(smtp_host_input.get_attribute("value"))
        smtp_host_input.send_keys("\b" * line_length)
        smtp_host_input.send_keys(smtp_host)

    def enter_smtp_port(self, smtp_port):
        smtp_port_input = self.wait.until(EC.presence_of_element_located((self.SMTP_PORT_INPUT)))
        line_length = len(smtp_port_input.get_attribute("value"))
        smtp_port_input.send_keys("\b" * line_length)
        smtp_port_input.send_keys(smtp_port)

    def enter_imap_username(self, imap_username):
        imap_username_input = self.wait.until(EC.presence_of_element_located((self.SMTP_USERNAME_INPUT)))
        line_length = len(imap_username_input.get_attribute("value"))
        imap_username_input.send_keys("\b" * line_length)
        imap_username_input.send_keys(imap_username)

    def enter_imap_password(self, imap_password):
        imap_password_input = self.wait.until(EC.presence_of_element_located((self.IMAP_PASSWORD_INPUT)))
        line_length = len(imap_password_input.get_attribute("value"))
        imap_password_input.send_keys("\b" * line_length)
        imap_password_input.send_keys(imap_password)

    def enter_imap_host(self, imap_host):
        imap_host_input = self.wait.until(EC.presence_of_element_located((self.IMAP_HOST_INPUT)))
        line_length = len(imap_host_input.get_attribute("value"))
        imap_host_input.send_keys("\b" * line_length)
        imap_host_input.send_keys(imap_host)

    def enter_imap_port(self, imap_port):
        imap_port_input = self.wait.until(EC.presence_of_element_located((self.IMAP_PORT_INPUT)))
        line_length = len(imap_port_input.get_attribute("value"))
        imap_port_input.send_keys("\b" * line_length)
        imap_port_input.send_keys(imap_port)

    def select_tariff_plan(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "vs__dropdown-toggle"))).click()
        self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, "li")))
        list_elements = self.driver.find_elements(By.TAG_NAME, "li")
        list_elements[0].click()

    def attach_mailbox(self):
        self.wait.until(EC.element_to_be_clickable((self.CONNECT_BUTTON))).click()

    def move_to_mailbox(self, email):
        self.wait.until(EC.element_to_be_clickable((By.ID, "Overview"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[contains(text(), '{email}')]"))).click()

    def disconnect_mailbox(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "settings_dialog_trigger"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "warmup-mode__btn--disconnect"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "float-label-select-wrap"))).click()
        self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, "li")))
        list_elements = self.driver.find_elements(By.TAG_NAME, "li")
        list_elements[0].click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "modal-footer__disconnect-btn"))).click()

    def is_connect_success(self, email):
        try:
            success_connect_marker = self.wait.until(EC.presence_of_element_located((self.SUCCESSFUL_CONNECT_MARKER)))
            return email in success_connect_marker.text
        except Exception as e:
            return False

    def is_connect_invalid_failed(self):
        try:
            error_invalid_connect_message = self.wait.until(EC.presence_of_element_located((self.FAILED_CONNECT_MARKER)))
            return ("Please check your email address and password and try again" or
                    "Invalid Username or Password for IMAP server" in error_invalid_connect_message.text)
        except Exception as e:
            return False

    def is_connect_existed_failed(self):
        try:
            error_existed_connect_message = self.wait.until(EC.presence_of_element_located((self.FAILED_CONNECT_MARKER)))
            return "This email is already used" in error_existed_connect_message.text
        except Exception as e:
            return False

    def is_connect_without_tariff_failed(self):
        try:
            error_without_tariff_connect_message = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".mailbox-regular-form > .relative > p")))
            return "This field is required" in error_without_tariff_connect_message.text
        except Exception as e:
            return False

    def is_disconnect_success(self, email):
        try:
            success_disconnect_marker = self.wait.until(EC.element_to_be_clickable((self.SUCCESSFUL_DISCONNECT_MARKER)))
            return email not in success_disconnect_marker.text
        except Exception as e:
            return False