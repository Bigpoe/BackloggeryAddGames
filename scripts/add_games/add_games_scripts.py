from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import config_data
from scripts.extract_data.extract_data import ExtractDataObj
from pages.login import LoginObj
from pages.dashboard import DashboardObj
from pages.new_game import NewGameObj


def test_add_games():
    
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get(config_data['url'])
    
    extract = ExtractDataObj()
    games_list = extract.extract_data_from_csv()

    login = LoginObj(driver)
    login.login_process(config_data['username'], config_data['valid_password'])

    dashboard = DashboardObj(driver)
    assert dashboard.logout_button
    dashboard.click_add_new_game_button()

    for row in games_list.index:
        game_name = games_list['game_name'][row]
        console_name = games_list['console_name'][row]
        progress_status = games_list['progress_status'][row]
        progress_notes = games_list['progress_notes'][row]
        now_playing = games_list['now_playing'][row]
        
        new_game = NewGameObj(driver)
        assert new_game.game_name_input

        new_game.add_new_game_process(
            game_name, 
            str(console_name), 
            progress_status, 
            progress_notes, 
            now_playing
            )
        print('\n')
        print(game_name, 'added to your Backloggery :D')
    
    # assert driver.find_element_by_css_selector("div .update-g"), 'Games added to your Backloggery :D'
