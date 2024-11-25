import unittest
from appium.webdriver.common.appiumby import AppiumBy
from Conection.conection import Driver
from Actions.deskClock import DeskClock


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Driver()
        
    def tearDown(self):
        self.driver.instance.quit()

    def test_add_alarm(self) -> None:
        alarmNavigationButton = 'com.google.android.deskclock:id/tab_menu_alarm'
        addButton = 'com.google.android.deskclock:id/fab'
        eightOClock = '//android.widget.TextView[@content-desc="8 o\'clock"]'
        amButton = 'com.google.android.deskclock:id/material_clock_period_am_button'
        okButton = 'com.google.android.deskclock:id/material_timepicker_ok_button'
        assertMessage = 'com.google.android.deskclock:id/snackbar_text'
        
        deskClock = DeskClock(self.driver)
        deskClock.clickByID(alarmNavigationButton)
        deskClock.clickByID(addButton)
        deskClock.clickByXpath(eightOClock)
        deskClock.clickByID(amButton)
        deskClock.clickByID(okButton)
        
        deskClock.assertIsVisibleById(assertMessage)
        
    def test_login_user_informations(self) -> None:
        alarmNavigationButton = 'com.google.android.deskclock:id/tab_menu_alarm'
        addButton = 'com.google.android.deskclock:id/fab'
        keyboardButton = 'com.google.android.deskclock:id/material_timepicker_mode_button'
        hourField = '//android.widget.EditText'
        okButton = 'com.google.android.deskclock:id/material_timepicker_ok_button'
        assertMessage = 'com.google.android.deskclock:id/snackbar_text'
        
        deskClock = DeskClock(self.driver)
        deskClock.clickByID(alarmNavigationButton)
        deskClock.clickByID(addButton)
        deskClock.waitElementById(keyboardButton)
        deskClock.clickByID(keyboardButton)
        deskClock.waitElementByXpath(hourField)
        deskClock.clearFieldByXpath(hourField)
        deskClock.clearFieldByXpath(hourField)
        deskClock.typeFieldByXpath(hourField, '09')
        deskClock.clickByID(okButton)
        
        deskClock.assertIsVisibleById(assertMessage)
        
if __name__ == '__main__':
    unittest.main()