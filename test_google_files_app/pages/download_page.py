from appium.webdriver.common.appiumby import AppiumBy


class DownloadPage:
    page_heading_xpath="(//*[@text='Downloads'])[2]"
    header_navigation_xpath= '//*[@content-desc="Show roots"]'
    header_search_accessibility_id= "Search"
    more_options_accessibility_id= 'More options'

    def __init__(self, driver):
        self.driver = driver

    def get_heading_text(self):
        heading_text = self.driver.find_element(AppiumBy.XPATH, self.page_heading_xpath).text
        return heading_text

    def verify_header_elements(self):
        # Store the boolean result of each check
        navigation_displayed = self.driver.find_element(AppiumBy.XPATH, self.header_navigation_xpath).is_displayed()
        search_displayed = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_search_accessibility_id).is_displayed()
        options_displayed = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.more_options_accessibility_id).is_displayed()
        heading_displayed = self.driver.find_element(AppiumBy.XPATH, self.page_heading_xpath).is_displayed()

        # Return True only if ALL are True
        return navigation_displayed and search_displayed and options_displayed and heading_displayed
