import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from random import randint

from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_list_page import EmployeeListPage
from steps.common import is_element_present


class AddEmployeeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 2)

        self.login_page = LoginPage(self.driver)
        self.menu = MenuPage(self.driver)
        self.add_employee = AddEmployeePage(self.driver)
        self.employee_list = EmployeeListPage(self.driver)

        self.driver.get('http://hrm.seleniumminutes.com')

    def tearDown(self):
        self.driver.quit()

    def test_add_employee(self):
        fake_data = Faker()
        emp_id = randint(100000, 999999)
        name = fake_data.name()
        sp_name = name.split()
        expected_first_name = sp_name[0]
        expected_last_name = sp_name[1]

        self.login_page.login()
        self.menu.add_employee()

        self.add_employee.add_employee(expected_first_name, expected_last_name, emp_id)

        self.menu.goto_employee_list()
        self.employee_list.search_employee(emp_id)

        actual_name = self.driver.find_element_by_link_text(expected_first_name).text
        self.assertEqual(expected_first_name, actual_name)


if __name__ == '__main__':
    unittest.main()
