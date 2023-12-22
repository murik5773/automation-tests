# base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")