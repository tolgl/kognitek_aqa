from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture
def driver():
    chrome_driver = ChromeDriverManager().install()
    service = Service(chrome_driver)
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options, service=service)

    yield driver

    driver.quit()
