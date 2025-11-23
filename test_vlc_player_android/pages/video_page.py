from appium.webdriver.common.appiumby import AppiumBy


class VideoPage:
    page_icon_id="toolbar_icon"
    page_toolbar_title_id= 'toolbar_vlc_title'
    header_search_accessibility_id= "Search…"
    header_display_sittings_accessibility_id= 'Display settings'
    header_more_options_accessibility_id= 'More options'

    tab_video_accessibility_id='videos'
    tab_playlist_xpath = '//android.widget.LinearLayout[@content-desc="Playlists"]'

    search_textfield_id= "search_src_text"
    search_textfield_clear_id= 'Clear query'
    empty_message_id = 'emptyTextView'
    message_text : str # No item found for search no match

    def __init__(self, driver):
        self.driver = driver

    def verify_heading_text_icon(self):
        self.driver.find_element(AppiumBy.ID, self.page_toolbar_title_id).is_displayed()
        self.driver.find_element(AppiumBy.ID, self.page_icon_id).is_displayed()
        title_text = self.driver.find_element(AppiumBy.ID, self.page_toolbar_title_id).text
        return title_text
