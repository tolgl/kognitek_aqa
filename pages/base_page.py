from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import BASE_URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    def go_to_page(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, wait_time=5):
        return WebDriverWait(self.driver, wait_time).until(expected_conditions.presence_of_element_located(locator))

    def wait_open_new_window(self, count, wait_time=5):
        WebDriverWait(self.driver, wait_time).until(
            expected_conditions.number_of_windows_to_be(count))

    def switch_to_window(self, count, index_win):
        self.wait_open_new_window(count)
        self.driver.switch_to.window(self.driver.window_handles[index_win])

    def close_window(self, count, index_win):
        self.wait_open_new_window(count)
        self.driver.switch_to.window(self.driver.window_handles[index_win])
        self.driver.close()

    def count_window(self):
        return len(self.driver.window_handles)
