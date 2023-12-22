# test_login.py

import pytest
from pages.login_page import LoginPage
from config.settings import USER_CREDENTIALS

@pytest.mark.parametrize("email,password", [
    (USER_CREDENTIALS['valid']['email'], USER_CREDENTIALS['valid']['password']),
    (USER_CREDENTIALS['invalid']['email'], USER_CREDENTIALS['valid']['password']),
    (USER_CREDENTIALS['valid']['email'], USER_CREDENTIALS['invalid']['password']),
    (USER_CREDENTIALS['invalid']['email'], USER_CREDENTIALS['invalid']['password']),
])

def test_login(driver, email, password):
    """
    Authorization tests with different combinations of email address and password.
    Need to add invalid email option
    """
    page = LoginPage(driver, driver.current_url)
    page.go_to_site()
    page.enter_email(email)
    page.enter_password(password)
    page.click_login_button()

    if email == USER_CREDENTIALS['valid']['email'] and password == USER_CREDENTIALS['valid']['password']:
        assert page.is_logged_in(), "User should be logged in with valid credentials"
    else:
        assert page.is_login_failed(), "Login should fail with invalid credentials"