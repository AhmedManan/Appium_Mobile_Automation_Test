import pytest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions

capabilities: Dict[str, Any] = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appPackage": "com.google.android.documentsui",
    "appActivity": "com.android.documentsui.files.FilesActivity",
    "appium:adbExecTimeout": 60000,
    "language": "en",
    "locale": "US"
}

url= "http://localhost:4723"

@pytest.fixture()
def driver():
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(capabilities))
    yield driver
    driver.quit()