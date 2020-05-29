class LoginObj:

    def __init__(self, driver):
        self.driver = driver
        self.username = driver.find_element_by_css_selector('#email')
        self.password = driver.find_element_by_css_selector('#password')
        self.login_button = driver.find_element_by_css_selector("input[value='Submit']")

    def login_process(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()