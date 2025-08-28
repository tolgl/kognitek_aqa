from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from config import BASE_URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    def go_to_page(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, wait_time=5):
        return WebDriverWait(self.driver, wait_time).until(expected_conditions.presence_of_element_located(locator))

    def switch_to_window(self, count, index_win, wait_time=5):
        WebDriverWait(self.driver, wait_time).until(
            expected_conditions.number_of_windows_to_be(count))
        self.driver.switch_to.window(self.driver.window_handles[index_win])

    def close_window(self, count, index_win):
        self.switch_to_window(count, index_win)
        self.driver.close()

    def count_window(self):
        return len(self.driver.window_handles)

    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def get_current_url(self):
        return self.driver.current_url

    def return_previous_page(self):
        self.driver.back()
