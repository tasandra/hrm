import unittest
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

from faker import Faker

from steps.common import login, get_welcome_message


class AddEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://hrm.seleniumminutes.com")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        fake_data = Faker()
        emp_id = randint(100000, 999999)
        name = fake_data.name()
        sp_name = name.split()
        expected_first_name = sp_name[0]
        expected_last_name = sp_name[1]

        # Login
        driver = self.driver

        login(driver)

        # assert welcome massage is present
        welcome_text = get_welcome_message(driver).text
        self.assertEqual('Welcome Admin', welcome_text)

        # Click the Add button
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_id("btnAdd").click()

        self.assertEquals("Add Employee", driver.find_element_by_tag_name("h1").text)

        # Enter First and Last name
        driver.find_element_by_id("firstName").send_keys(expected_first_name)
        driver.find_element_by_id("lastName").send_keys(expected_last_name)

        # Enter the empID
        driver.find_element_by_id("employeeId").clear()
        driver.find_element_by_id("employeeId").send_keys(emp_id)

        # Save the Employee
        driver.find_element_by_id("btnSave").click()

        # Go to PIM page
        driver.find_element_by_id("menu_pim_viewPimModule").click()

        # Search by empID
        driver.find_element_by_id("empsearch_id").send_keys(emp_id)
        driver.find_element_by_id("searchBtn").click()

        # Expected: 1 record back
        _first_names = driver.find_elements_by_xpath("//*[@id='resultTable']/tbody/tr/td[3]/a")
        self.assertTrue(len(_first_names) == 1)

        # Edit employee
        driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr/td[3]/a").click()
        driver.find_element_by_xpath("//*[@id='sidenav']/li[6]/a").click()
        driver.find_element_by_id("btnSave").click()

        job_index = randint(0, 5)
        locator1 = (By.ID, "job_job_title")
        self.wait.until(expected_conditions.presence_of_element_located(locator1))
        Select(driver.find_element_by_id("job_job_title")).select_by_index(job_index)
        job_title = Select(driver.find_element_by_id("job_job_title")).first_selected_option.text

        driver.find_element_by_id("btnSave").click()
        locator2 = (By.CSS_SELECTOR, ".message.success")
        self.wait.until(expected_conditions.presence_of_element_located(locator2))

        # Expected correct Name and job title
        name = driver.find_element_by_xpath("//*[@id='profile-pic']/h1").text
        expected_name = expected_first_name + " " + expected_last_name
        message = "Expected the table to contain name {0} but instead the value was {1}"
        self.assertEquals(expected_name, name, message.format(expected_name, name))
        self.assertEquals(job_title, Select(driver.find_element_by_id("job_job_title")).first_selected_option.text)


if __name__ == '__main__':
    unittest.main()

