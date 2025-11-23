from ..conftest import driver
from ..pages.video_page import VideoPage

class TestVideoPage:

    def test_icon_title_verification(self, driver):
        driver = driver
        self.video_page = VideoPage(driver)
        assert self.video_page.verify_heading_text_icon() == "VLC"