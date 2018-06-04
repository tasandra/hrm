import unittest
from selenium import webdriver


class Login_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("http://hrm.seleniumminutes.com")

    def test_valid_log_in(self):
        driver = self.driver
        self.assertEquals("OrangeHRM", driver.title)

        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("Password")
        driver.find_element_by_id("btnLogin").submit()

        # assert welcome massage is present
        self.assertEquals("Welcome Admin", driver.find_element_by_id("welcome").text)

        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text("Logout").click()

        # assert user get back to login page after logout form application
        self.assertTrue(driver.find_element_by_id("divLoginButton").is_displayed())

    def test_invalid_password_login(self):
        driver = self.driver
        self.assertEquals("OrangeHRM", driver.title)

        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("password")
        driver.find_element_by_id("btnLogin").submit()

        # assert error massage
        self.assertEquals("Invalid credentials", driver.find_element_by_id("spanMessage").text)

    def test_empty_password_login(self):
        driver = self.driver
        self.assertEquals("OrangeHRM", driver.title)

        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("")
        driver.find_element_by_id("btnLogin").submit()

        # assert error massage
        self.assertEquals("Password cannot be empty", driver.find_element_by_id("spanMessage").text)

    def tearDown(self):
        self.driver.quit


if __name__ == '__main__':
    unittest.main()
