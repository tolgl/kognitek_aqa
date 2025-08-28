from pages.base_page import BasePage
from locators.popup_window_locators import PopupWindowLocators


class PopupWindowPageHelper(BasePage):

    def get_text_h3(self):
        return self.find_element(PopupWindowLocators.h3).text
