from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPageHelper(BasePage):

    def check_status_checkbox_orange(self):
        return self.find_element(MainPageLocators.checkbox_orange).is_selected()
