class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username='admin', password='Password'):
        driver = self.driver
        if driver.current_url.find('seleniumminutes') >= 0 and username == 'admin':
            password = password.title()

        driver.find_element_by_id('txtUsername').send_keys(username)
        driver.find_element_by_id('txtPassword').send_keys(password)
        driver.find_element_by_id('btnLogin').click()

    def get_warning_message(self):
        return self.driver.find_element_by_id('spanMessage').text
