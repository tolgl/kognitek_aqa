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

    def double_click_on_text(self):
        element = self.find_element(MainPageLocators.text_double_click)
        self.double_click(element)

    def get_class_context_menu(self):
        return self.find_element(MainPageLocators.context_menu).get_attribute("class")

    def click_link_gmail_context_menu(self):
        self.find_element(MainPageLocators.context_menu_link_gmail).click()
