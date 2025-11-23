from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from video_page import VideoPage

class VideoPlayerPage:

    player_surface_id = 'player_surface_frame'
    player_play_button_accessibility_id = 'Play'
    player_pause_button_accessibility_id='Pause'
    player_overlay_volume_text_id='player_overlay_volume'
    player_volume_progress_indicator_id='playerVolumeProgress'
    player_volume_icon_id='progress_icon'
    player_volume_value_text_id='volume_value_text'
    player_overlay_time_id = 'player_overlay_time'
    player_overlay_length_id='player_overlay_length'
    player_overlay_title_id='player_overlay_title'
    player_hub_background_id = 'hud_background'
    player_progress_overlay_id = 'progress_overlay'
    player_resizer_accessibility_id='Aspect ratio'
    player_advanced_option_accessibility_id='advanced options'
    player_orientation_id='orientation_toggle'
    player_orientation_accessibility_id='unlock orientation'
    player_overlay_tracks_id='player_overlay_tracks'

    def __init__(self, driver):
        self.driver = driver
        self.video_page = VideoPage(driver)
        self.driver.find_element(AppiumBy.XPATH, self.video_page.venom_video_xpath).click()

    def check_video_player(self):
        player_surface_locator= self.driver.find_element(AppiumBy.ID, self.player_surface_id)
        player_surface_displayed = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(player_surface_locator))
        return player_surface_displayed


