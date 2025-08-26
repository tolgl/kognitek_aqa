from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPageHelper(BasePage):

    def check_status_checkbox_orange(self):
        return self.find_element(MainPageLocators.checkbox_orange).is_selected()

    def click_checkbox_blue(self):
        self.find_element(MainPageLocators.checkbox_blue).click()

    def check_status_checkbox_blue(self):
        return self.find_element(MainPageLocators.checkbox_blue).is_selected()

    def click_button_open_new_window(self):
        self.find_element(MainPageLocators.button_open_new_window).click()
