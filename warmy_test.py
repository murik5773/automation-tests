import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

class TestsWarmy(unittest.TestCase):

  def setUp(self):
    options = Options()
#    options.add_argument('headless')
    options.add_argument("--start-maximized")
    options.page_load_strategy = "eager"
    self.url = "https://www.warmy.io/"
    self.url_signin = "https://www.warmy.io/signin"
#    self.login = "murik5773+2000@gmail.com"
#    self.password = "111111"
    service = Service(executable_path="chromedriver.exe")
    self.driver = webdriver.Chrome(service=service, options=options)
    self.wait = WebDriverWait(self.driver, timeout=10)
  
  def test_17_sign_in_facebook(self):
    print("\tSign in")
    driver = self.driver
    wait = self.wait
    driver.get(self.url)
    print("\tSuccess")
  
  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()