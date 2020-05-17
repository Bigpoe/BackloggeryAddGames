from selenium.webdriver.common.keys import Keys

class NewGameObj:

    def __init__(self, driver):
        self.driver = driver
        self.game_name_input = driver.find_element_by_css_selector("input[name='name']")
        self.select_console_selector = driver.find_element_by_css_selector("select[name='console']")
        
        ## Progress status ##
        self.unfinished = driver.find_element_by_css_selector("fieldset div label img[src*='unfinished.gif']")
        self.unfinished = driver.find_element_by_css_selector("#complete1")
        self.beaten = driver.find_element_by_css_selector("#complete2")
        self.completed = driver.find_element_by_css_selector("#complete3")
        self.null = driver.find_element_by_css_selector("#complete4")
        self.mastered = driver.find_element_by_css_selector("#complete5")
        self.unplayed = driver.find_element_by_css_selector("#unplayed_group")
        self.progress_notes_filed = driver.find_element_by_css_selector("input[name='note']")

        self.now_playing_check = driver.find_element_by_css_selector("#npcheck")
        self.whishlist_check = driver.find_element_by_css_selector("#wishcheck")
        self.add_game_button = driver.find_element_by_css_selector("div input[value='Add Game']")
        self.stealh_add_button = driver.find_element_by_css_selector("div input[value='Stealth Add']")
        
    def add_new_game_process(self, game, console_name, progress_status, progress_notes, now_playing):
        self.game_name_input.send_keys(game)
        
        ## Select the desired console ##
        select_console = self.select_console_selector
        for option in select_console.find_elements_by_tag_name('option'):
            if option.text == console_name:
                option.click()
                break

        ## Select progress status ##
        if progress_status == 'Unfinished':
            self.unfinished.click()
        elif progress_status == 'Beaten':
            self.beaten.click()
        elif progress_status == 'Completed':
            self.completed.click()
        elif progress_status == 'Null':
            self.null.click()
        elif progress_status == 'Mastered':
            self.mastered.click()
        elif progress_status == '':
            pass

        ## Add progress notes ##
        self.progress_notes_filed.send_keys(progress_notes)

        ## Mark game as 'playing now' ##
        if now_playing == '1':
            self.now_playing_check.click()
        elif now_playing == '0':
            pass

        ## Add game to wishlist ##
        if now_playing == '1':
            self.now_playing_check.click()
        elif now_playing == '0':
            pass

        ## Save the game ##
        self.add_game_button.click()
