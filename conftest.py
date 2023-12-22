# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config.settings import BASE_URL, DRIVER_PATHS

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    url = BASE_URL[request.config.getoption("--env")]

    if browser == 'chrome':
        service = ChromeService(executable_path=DRIVER_PATHS['chrome'])
        chrome_options = ChromeOptions()
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
    elif browser == 'firefox':
        service = FirefoxService(executable_path=DRIVER_PATHS['firefox'])
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=firefox_options)
        driver.maximize_window()
    else:
        raise ValueError(f"Browser {browser} not supported")

    driver.get(url)
    yield driver
    driver.quit()

# options for pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="choose your browser: chrome or firefox"
    )
    
    parser.addoption(
        "--env",
        action="store",
        default="production",
        help="choose your environment: test, staging, production"
    )