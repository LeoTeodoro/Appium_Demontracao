from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

class DeskClock:
    def __init__(self, driver):
        self.driver = driver
        
    def assertEqualsTextById(self, id, message):
        try:
            element = self.driver.instance.find_element(by=AppiumBy.ID, value=id)
            assert element.text == message, f"Elemento com ID '{id}' não está igual ao texto '{message}'."
            return True
        except NoSuchElementException:
            raise AssertionError(f"Elemento com ID '{id}' não foi encontrado.")
    
    def assertEqualsTextByXpath(self, xpath, message):
        try:
            element = self.driver.instance.find_element(by=AppiumBy.XPATH, value=xpath)
            assert element.text == message, f"Elemento com XPATH '{xpath}' não está igual ao texto '{message}'."
            return True
        except NoSuchElementException:
            raise AssertionError(f"Elemento com XPATH '{xpath}' não foi encontrado.")
    
    def assertIsVisibleById(self, id):
        try:
            element = self.driver.instance.find_element(by=AppiumBy.ID, value=id)
            assert element.is_displayed(), f"Elemento com ID '{id}' não está visível."
            return True
        except NoSuchElementException:
            raise AssertionError(f"Elemento com ID '{id}' não foi encontrado.")

        
    def waitElementById(self, id):
        self.permission = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, id))
        )
        
    def waitElementByXpath(self, xpath):
        self.permission = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, xpath))
        )
        
    def clickByID(self, id):
        button = self.driver.instance.find_element(by=AppiumBy.ID, value=id)
        button.click()
        
    def clickByXpath(self, xpath):
        button = self.driver.instance.find_element(by=AppiumBy.XPATH, value=xpath)
        button.click()
        
    def clickByAccessibilityId(self, accessibilityId):
        button = self.driver.instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=accessibilityId)
        button.click()
        
    def typeFieldByXpath(self, xpath, message):
        field = self.driver.instance.find_element(by=AppiumBy.XPATH, value=xpath)
        field.send_keys(message)
        
    def clearFieldByXpath(self, xpath):
        field = self.driver.instance.find_element(by=AppiumBy.XPATH, value=xpath)
        field.clear()
  
