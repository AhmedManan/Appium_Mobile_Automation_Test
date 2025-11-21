from ..conftest import driver
from ..pages.download_page import DownloadPage


class TestDownloadPage():

    def test_title_verification(self, driver):
        driver = driver
        self.download_page = DownloadPage(driver)
        assert self.download_page.get_heading_text() == "Downloads"

    def test_header_elements(self, driver):
        driver = driver
        self.download_page = DownloadPage(driver)
        assert self.download_page.verify_header_elements()