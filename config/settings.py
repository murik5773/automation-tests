# settings.py

# Basic environments
BASE_URL = {
    "testing": "https://testing.warmy.io/",
    "test": "https://test.warmy.io/signin",
    "staging": "https://staging.warmy.io/signin",
    "production": "https://www.warmy.io/signin"
}

# Credentials for login
USER_CREDENTIALS = {
    "valid": {
        "email": "anthony.stark.5773@gmail.com",
        "password": "BNe729gn9U"
    },
    "invalid": {
        "email": "anthony.stark@gmail.com",
        "password": "BNe729gn9A"
    }
}

# Options for different browsers
DRIVER_PATHS = {
    "chrome": "./drivers/chromedriver.exe",
    "firefox": "./drivers/geckodriver.exe"
}