from selenium.webdriver.common.keys import Keys

class NewGameObj:

    def __init__(self, driver):
        self.driver = driver

        self.mode_toggle = driver.find_element_by_css_selector("input[value='Toggle']")
        self.game_name_input = driver.find_element_by_css_selector("input[name='name']")
        self.compilation_input = driver.find_element_by_css_selector("input[name='comp']")
        self.system_selector = driver.find_element_by_css_selector("select[name='console']")
        self.original_system_selector = driver.find_element_by_css_selector("select[name='orig_console']")
        self.region_selector = driver.find_element_by_css_selector("select[name='region']")
        ## Ownership ##
        self.owned = driver.find_element_by_css_selector("#own1")
        self.household = driver.find_element_by_css_selector("#own5")
        self.subscription = driver.find_element_by_css_selector("#own6")
        self.borrowed_rented = driver.find_element_by_css_selector("#own3")
        self.formerly_owned = driver.find_element_by_css_selector("#own2")
        self.other = driver.find_element_by_css_selector("#own4")
        ## Progress status ##
        #self.unfinished = driver.find_element_by_css_selector("fieldset div label img[src*='unfinished.gif']")
        self.unfinished = driver.find_element_by_css_selector("#complete1")
        self.beaten = driver.find_element_by_css_selector("#complete2")
        self.completed = driver.find_element_by_css_selector("#complete3")
        self.null = driver.find_element_by_css_selector("#complete4")
        self.mastered = driver.find_element_by_css_selector("#complete5")
        self.unplayed = driver.find_element_by_css_selector("#unplayed_group")

        self.achievements1_input = driver.find_element_by_css_selector("input[name='achieve1']")
        self.achievements2_input = driver.find_element_by_css_selector("input[name='achieve2']")
        self.online_info_input = driver.find_element_by_css_selector("input[name='online']")
        self.progress_notes_input = driver.find_element_by_css_selector("input[name='note']")
        
        self.rating_5_radio_button = driver.find_element_by_css_selector("#rating4")
        self.rating_4_radio_button = driver.find_element_by_css_selector("#rating3")
        self.rating_3_radio_button = driver.find_element_by_css_selector("#rating2")
        self.rating_2_radio_button = driver.find_element_by_css_selector("#rating1")
        self.rating_1_radio_button = driver.find_element_by_css_selector("#rating0")
        self.no_rating_radio_button = driver.find_element_by_css_selector("#rating8")
        self.commets_input = driver.find_element_by_css_selector("#comments")

        self.now_playing_check = driver.find_element_by_css_selector("#npcheck")
        self.whishlist_check = driver.find_element_by_css_selector("#wishcheck")
        self.add_game_button = driver.find_element_by_css_selector("div input[value='Add Game']")
        self.stealh_add_button = driver.find_element_by_css_selector("div input[value='Stealth Add']")
        

    def fill_game_information_process(self, game_name, compilation, system, original_system, region, ownership):
        self.game_name_input.send_keys(game_name)
        self.compilation_input.send_keys(compilation)
         
        ## Select console ##
        select_console = self.system_selector
        for option in select_console.find_elements_by_tag_name('option'):
            if option.text == system:
                option.click()
                break
        
        ## Select original system ##
        original_systemm = self.original_system_selector
        for option in original_systemm.find_elements_by_tag_name('option'):
            if option.text == original_system:
                option.click()
                break

        ## Select region ##
        select_region = self.region_selector
        for option in select_region.find_elements_by_tag_name('option'):
            if option.text == region:
                option.click()
                break

        ## Select ownership ##
        if ownership == 'Owned' or ownership == 'owned':
            self.owned.click()
        elif ownership == 'Household' or ownership == 'household':
            self.household.click()
        elif ownership == 'Subscription' or ownership == 'subscription':
            self.subscription.click()
        elif ownership == 'Borrowed/Rented' or ownership == 'borrowed/rented':
            self.borrowed_rented.click()
        elif ownership == 'Formerly Owned' or ownership == 'formerly owned':
            self.formerly_owned.click()
        elif ownership == 'Other' or ownership == 'other':
            self.other.click()
        elif ownership == '':
            pass

    def fill_progress_process(self, progress_status, achievements1, achievements2, online_info, progress_notes):
         ## Select progress status ##
        if progress_status == 'Unfinished' or progress_status == 'unfinished':
            self.unfinished.click()
        elif progress_status == 'Beaten' or progress_status == 'beaten':
            self.beaten.click()
        elif progress_status == 'Completed' or progress_status == 'completed':
            self.completed.click()
        elif progress_status == 'Null' or progress_status == 'null':
            self.null.click()
        elif progress_status == 'Mastered' or progress_status == 'mastered':
            self.mastered.click()
        elif progress_status == '':
            pass

        self.achievements1_input.send_keys(achievements1)
        self.achievements2_input.send_keys(achievements2)
        self.online_info_input.send_keys(online_info)
        self.progress_notes_input.send_keys(progress_notes)

    def fill_review_process(self, rating, review_comments):
        ## Select rating level ##
        if rating == '5':
            self.rating_5_radio_button.click()
        elif rating == '4':
            self.rating_4_radio_button.click()
        elif rating == '3':
            self.rating_3_radio_button.click()
        elif rating == '2':
            self.rating_2_radio_button.click()
        elif rating == '1':
            self.rating_1_radio_button.click()
        elif rating == '0' or rating == '':
            self.no_rating_radio_button.click()

        self.commets_input.send_keys(review_comments)


################ Add games methods ################

    ## Add new game detailed mode process ##
    def add_new_game_detailed_mode_process(
            self, 
            game_name,
            compilation,
            system, 
            original_system,
            region,
            ownership,
            progress_status,
            achievements1,
            achievements2,
            online_info,
            progress_notes,
            rating_radio,
            review_comments,
            now_playing, 
            whishlist
            ): 

        self.mode_toggle.click()
        self.fill_game_information_process(game_name, compilation, system, original_system, region, ownership)
        self.fill_progress_process(progress_status, achievements1, achievements2, online_info, progress_notes)
        self.fill_review_process(rating_radio, review_comments)

         ## Mark game as 'playing now' ##
        if now_playing == '1':
            self.now_playing_check.click()
        elif now_playing == '0' or now_playing == '':
            pass

        ## Add game to wishlist ##
        if whishlist == '1':
            self.whishlist_check.click()
        elif whishlist == '0' or now_playing == '':
            pass

        ## Save the game ##
        self.add_game_button.click()


    ## Add new game simple mode process ##

    def add_new_game_simple_mode_process(self, game_name, system, progress_status, progress_notes, now_playing, whishlist):
        self.game_name_input.send_keys(game_name)

        ## Select the desired console ##
        select_console = self.system_selector
        for option in select_console.find_elements_by_tag_name('option'):
            if option.text == system:
                option.click()
                break

        ## Select progress status ##
        if progress_status == 'Unfinished' or progress_status == 'unfinished':
            self.unfinished.click()
        elif progress_status == 'Beaten' or progress_status == 'beaten':
            self.beaten.click()
        elif progress_status == 'Completed' or progress_status == 'completed':
            self.completed.click()
        elif progress_status == 'Null' or progress_status == 'null':
            self.null.click()
        elif progress_status == 'Mastered' or progress_status == 'mastered':
            self.mastered.click()
        elif progress_status == '':
            pass

        ## Add progress notes ##
        self.progress_notes_input.send_keys(progress_notes)

        ## Mark game as 'playing now' ##
        if now_playing == '1':
            self.now_playing_check.click()
        elif now_playing == '0' or now_playing == '':
            pass

        ## Add game to wishlist ##
        if whishlist == '1':
            self.whishlist_check.click()
        elif whishlist == '0' or now_playing == '':
            pass

        ## Save the game ##
        self.add_game_button.click()