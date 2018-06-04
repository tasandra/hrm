from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

locators = {
    "pim": (By.ID, "menu_pim_viewPimModule"),
    "add_employee": (By.ID, "menu_pim_addEmployee"),
    "employee_list": (By.ID, "menu_pim_viewEmployeeList"),
    "reports": (By.ID, "menu_core_viewDefinedPredefinedReports"),
}


class MenuPage(BasePage):

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver)
        self.page_url = "http://hrm.seleniumminutes.com/symfony/web/index.php/dashboard"

    def add_employee(self):
        menu = self.driver.find_element_by_id(locators["pim"][1])
        hidden_submenu = self.driver.find_element_by_id(locators["add_employee"][1])

        actions = ActionChains(self.driver)
        actions.move_to_element(menu)
        actions.click(hidden_submenu)
        actions.perform()

    def goto_employee_list(self):
        self.driver.find_element_by_id(locators["employee_list"][1]).click()
