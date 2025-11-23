from ..conftest import driver
from ..pages.video_page import VideoPage

class TestVideoPage:

    def test_icon_title_verification(self, driver):
        driver = driver
        self.video_page = VideoPage(driver)
        assert self.video_page.verify_heading_title() == "VLC"

    def test_navigation_elements(self, driver):
        driver = driver
        self.video_page = VideoPage(driver)
        assert self.video_page.verify_navigation_elements()

    def test_header_search_functionality(self, driver):
        driver = driver
        self.video_page = VideoPage(driver)
        assert self.video_page.check_header_search_functionality(search_text="no match")
        assert self.video_page.message_text == "No item found for search no match"