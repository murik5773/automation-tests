# login_page.py

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (By.CLASS_NAME, "custom-btn--2")
    SUCCESSFUL_LOGIN_MARKER = (By.ID, "Logout")
    FAILED_LOGIN_MARKER = (By.CSS_SELECTOR, ".login-form > .regular-feedback > .regular-feedback__content > span")

    def enter_email(self, email):
        email_input = self.wait.until(EC.presence_of_element_located((self.EMAIL_INPUT)))
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.wait.until(EC.presence_of_element_located((self.PASSWORD_INPUT)))
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable((self.LOGIN_BUTTON)))
        login_button.click()

    def is_logged_in(self):
        try:
            success_marker = self.wait.until(EC.element_to_be_clickable((self.SUCCESSFUL_LOGIN_MARKER)))
            return True
        except Exception as e:
            return False

    def is_login_failed(self):
        try:
            error_message = self.wait.until(EC.presence_of_element_located((self.FAILED_LOGIN_MARKER)))
            return "Invalid login credentials. Please try again." in error_message.text
        except Exception as e:
            return False