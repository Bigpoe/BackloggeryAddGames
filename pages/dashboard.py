from selenium.webdriver.common.action_chains import ActionChains

class DashboardObj:

    def __init__(self, driver):
        self.driver = driver
        self.logout_button = driver.find_element_by_css_selector("#logout")
        self.my_games = driver.find_element_by_css_selector("#menu > ul:nth-child(2) > li:nth-child(3) > a")
        self.add_new_game_button = driver.find_element_by_css_selector("#menu > ul:nth-child(2) > li:nth-child(3) > ul > li > a[href*='newgame.php']")

    def click_add_new_game_button(self):
        hover = ActionChains(self.driver).move_to_element(self.my_games)
        hover.perform()
        self.add_new_game_button.click()

    