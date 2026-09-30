from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import tempfile


@pytest.fixture
def driver():

    chrome_options = Options()

    # Perfil limpo e isolado
    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    # Desativa Password Manager
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }

    chrome_options.add_experimental_option("prefs", prefs)

    chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    chrome_options.add_argument("--safebrowsing-disable-leak-detection")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()

    yield driver

    driver.quit()
