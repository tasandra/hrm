import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '5710345c61d73e4d4501706088d10ba9affa1566'
        self.dc['platformName'] = 'ios'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)
        self.wait = WebDriverWait(self.driver, 30)

    def testUntitled(self):
        self.driver.find_element_by_id("Calendar").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Saturday, July 7']").click()
        self.wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='Gelena']")))
        event = self.driver.find_element_by_xpath("(//*/*[@text and @class='UIAStaticText'])[3]").text
        self.assertEqual("Gelena", event, "Event title is not correct")

        self.driver.find_element_by_id("Inbox").click()
        self.wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "(//*[@class='UIAStaticText']/*[@class='UIAButton'])[1]")))
        new_button = self.driver.find_element_by_xpath("(//*[@class='UIAStaticText']/*[@class='UIAButton'])[1]").text

        self.assertEqual("New", new_button, "New button is not present")

        self.driver.find_element_by_xpath("//*[@text='Done']").click()
        self.driver.execute_script("seetest:client.deviceAction(\"Home\")")

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
