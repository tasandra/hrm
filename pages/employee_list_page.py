from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

locators = {
    "employee_id": (By.ID, "empsearch_id"),
    "search_button": (By.ID, "searchBtn"),
    "list": (By.XPATH, "//*[@id='resultTable']/tbody/tr/td/a")
}


class EmployeeListPage(BasePage):

    def __init__(self, driver):
        super(EmployeeListPage, self).__init__(driver)
        self.page_url = "http://hrm.seleniumminutes.com/symfony/web/index.php/pim/viewEmployeeList"

    def search_employee(self, emp_id):
        self.driver.find_element_by_id(locators["employee_id"][1]).clear()
        self.driver.find_element_by_id(locators["employee_id"][1]).send_keys(emp_id)
        self.driver.find_element_by_id(locators["search_button"][1]).click()

    def get_employee_list(self):
        return self.wait.until(EC.visibility_of_all_elements_located_located((By.XPATH, locators["list"])))

