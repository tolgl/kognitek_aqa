from pages.main_page import MainPageHelper


class TestSearchBlog:

    def test_search_blog(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.filling_field_search(query='post')
        main_page.click_button_search()

        assert "search?q=post" in main_page.get_current_url()
        assert "No posts matching the query" in main_page.get_text_result_search()
