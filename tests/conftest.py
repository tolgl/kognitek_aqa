from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest

from pages.base_page import BasePage
from pages.main_page import MainPageHelper


@pytest.fixture
def driver():
    chrome_driver = ChromeDriverManager().install()
    service = Service(chrome_driver)
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options, service=service)

    yield driver

    driver.quit()


@pytest.fixture()
def double_click_on_text(driver):
    base_page = BasePage(driver)
    base_page.go_to_page()
    main_page = MainPageHelper(driver)
    main_page.double_click_on_text()
