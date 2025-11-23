from ..conftest import driver
from ..pages.video_player_page import VideoPlayerPage

class TestPlayerTest:

    def test_video_player(self, driver):
        self.driver = driver
        self.video_player_page = VideoPlayerPage(driver)
        assert self.video_player_page.check_video_player()