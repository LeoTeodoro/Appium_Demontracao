from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions

class Driver:
    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "avd": "Appium",
            "appPackage": "com.google.android.deskclock",
            "appActivity": "com.android.deskclock.DeskClock",
            "deviceName": "emulator-5554",
            "platformVersion": "15"
        }
        url = 'http://localhost:4723'
        options = AppiumOptions().load_capabilities(desired_cap)
        self.instance = webdriver.Remote(url, options=options)
        print("\rConectado")
