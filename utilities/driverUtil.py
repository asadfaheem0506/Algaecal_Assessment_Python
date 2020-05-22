from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utilities.settings import settings

class Driver(object):
    instance = None
    browser = None

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        print('---------' + settings.browser + '---------')
        if settings.browser == "chrome":
            self.driver = webdriver.Chrome('chromedriver')

    def get_driver(self):
        return self.drive

    def navigate(self, url):
        self.driver.get(url)

    def waitOnElement(self, elemXpath):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, elemXpath)))

    def waitFor(self, timeInSec):
        self.driver.implicitly_wait(timeInSec)

    def elementClick(self, elemXpath):
        return self.driver.find_element_by_xpath(elemXpath).click()

    def enterValues(self, elemXpath, value):
        return self.driver.find_element_by_xpath(elemXpath).send_keys(value)

    def getTextForElement(self, element):
        return self.driver.find_element_by_xpath(element).text

    def closeBrowser(self):
        self.driver.quit()

driver = Driver.get_instance()