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
    search_clear_query_id= 'search_close_btn'
    search_close_accessibility_id= 'Collapse'

    display_settings_page_header_id="title"

    more_options_dropdown_uiautomator = 'new UiSelector().className("android.widget.FrameLayout").instance(1)'

    page_first_video_xpath = '(//android.widget.ImageView[@resource-id="org.videolan.vlc:id/ml_item_thumbnail"])[1]'
    venom_video_xpath= '//android.widget.TextView[@resource-id="org.videolan.vlc:id/ml_item_title" and @text="VENOM THE LAST DANCE – Official Trailer (HD)"]'

    def __init__(self, driver):
        self.driver = driver

    def verify_heading_title(self):
        title = self.driver.find_element(AppiumBy.ID, self.page_toolbar_title_id)
        title_text = title.text
        return title_text

    def verify_navigation_elements(self):
        icon_displayed=self.driver.find_element(AppiumBy.ID, self.page_icon_id).is_displayed()
        title_displayed=self.driver.find_element(AppiumBy.ID, self.page_toolbar_title_id).is_displayed()
        search_displayed=self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_search_accessibility_id).is_displayed()
        display_settings_displayed=self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_display_sittings_accessibility_id).is_displayed()
        more_options_displayed=self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_more_options_accessibility_id).is_displayed()

        return icon_displayed and title_displayed and search_displayed and display_settings_displayed and more_options_displayed

    def check_header_search_functionality(self, search_text:str):
        clickable = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_search_accessibility_id).is_enabled()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_search_accessibility_id).click()
        self.driver.find_element(AppiumBy.ID, self.search_textfield_id).send_keys(search_text)
        self.driver.find_element(AppiumBy.ID, self.empty_message_id).is_displayed()
        self.message_text = self.driver.find_element(AppiumBy.ID, self.empty_message_id).text
        self.driver.find_element(AppiumBy.ID, self.search_clear_query_id).click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.search_close_accessibility_id).click()

        return clickable

    def check_header_display_settings_functionality(self):
        clickable = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_display_sittings_accessibility_id).is_enabled()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_display_sittings_accessibility_id).click()
        settings_page_displayed=self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_display_sittings_accessibility_id).is_displayed()

        return clickable and settings_page_displayed

    def check_header_more_options_functionality(self):
        clickable = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_more_options_accessibility_id).is_enabled()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_more_options_accessibility_id).click()
        more_option_displayed = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.more_options_dropdown_uiautomator).is_displayed()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_more_options_accessibility_id).click()

        return clickable and more_option_displayed

    def check_video_thumbnail_functionality(self):
        clickable = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.page_first_video_xpath).is_enabled()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.page_first_video_xpath).click()
        video_load = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.page_icon_id).is_displayed(False)

        return clickable and video_load