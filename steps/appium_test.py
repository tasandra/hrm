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
        self.driver.execute_script("seetest:client.deviceAction('Home')")
        self.driver.execute_script("seetest:client.deviceAction('Home')")
        self.wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='Touch ID or Enter Passcode']")))
        self.driver.find_element_by_xpath("//*[@text='8']").click()
        self.driver.find_element_by_xpath("//*[@text='6']").click()
        self.driver.find_element_by_xpath("//*[@text='8']").click()
        self.driver.find_element_by_xpath("//*[@text='9']").click()
        self.driver.find_element_by_xpath("//*[@text='Calendar']").click()
        self.driver.find_element_by_xpath("((//*[@class='UIAScrollView']/*[@class='UIAView'])[4]/*[@class='UIAButton'])[1]").click()
        self.driver.find_element_by_xpath("(//*/*[@text and @class='UIAStaticText'])[2]").click()
        self.wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "(//*/*[@class='UIAStaticText'])[1]")))
        label = self.driver.find_element_by_xpath("(//*/*[@class='UIAStaticText'])[1]").text
        self.assertEqual("Father's Day", label)
        date = self.driver.find_element_by_xpath("(//*/*[@class='UIAStaticText'])[2]").text
        self.assertEqual("Sunday, Jun 17, 2018", date)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
