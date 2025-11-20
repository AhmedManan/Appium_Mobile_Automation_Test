from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

capabilities: Dict[str, Any] = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "appium:adbExecTimeout": 60000,
    "language": "en",
    "locale": "US"
}

url= "http://localhost:4723"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(capabilities))
driver.find_element(AppiumBy.XPATH, "//*[@text='Apps']").click()
driver.save_screenshot("screenshot.png")
driver.quit()