from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

locators = {
    "first_name": (By.ID, "firstName"),
    "last_name": (By.ID, "lastName"),
    "employee_id": (By.ID, "employeeId"),
    "btn_save": (By.ID, "btnSave"),
}


class AddEmployeePage(BasePage):

    def __init__(self, driver):
        super(AddEmployeePage, self).__init__(driver)
        self.page_url = "http://hrm.seleniumminutes.com/symfony/web/index.php/pim/addEmployee"

    def add_employee(self, first_name, last_name, emp_id):
        self.driver.find_element_by_id(locators["first_name"][1]).send_keys(first_name)
        self.driver.find_element_by_id(locators["last_name"][1]).send_keys(last_name)
        self.driver.find_element_by_id(locators["employee_id"][1]).clear()
        self.driver.find_element_by_id(locators["employee_id"][1]).send_keys(emp_id)
        self.driver.find_element_by_id(locators["btn_save"][1]).click()
