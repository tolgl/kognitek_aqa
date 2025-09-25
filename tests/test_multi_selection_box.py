import pytest

from pages.main_page import MainPageHelper


class TestMultiSelectionBox:

    @pytest.mark.parametrize("start_index,final_index",
                             [
                                [1, 3],
                                [0, 2],
                                [2, 4]
                             ]
                             )
    def test_select_two_elements(self, driver, start_index, final_index):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.select_element_by_multi_selection_box(start_index=start_index, final_index=final_index)
