from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config.config import config_data
from ..extract_data_module.extract_data import ExtractDataObj
from pages.login import LoginObj
from pages.dashboard import DashboardObj
from pages.new_game import NewGameObj


def test_add_games_detailed():
    
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get(config_data['url'])
    
    extract = ExtractDataObj()
    games_list = extract.extract_detailed_data_from_csv()

    login = LoginObj(driver)
    login.login_process(config_data['username'], config_data['password'])

    dashboard = DashboardObj(driver)
    assert dashboard.logout_button
    dashboard.click_add_new_game_button()

    for row in games_list.index:
        game_name = games_list['game_name'][row]
        compilation = games_list['compilation'][row]
        system = games_list['system'][row]
        original_system = games_list['original_system'][row]
        region = games_list['region'][row]
        ownership = games_list['ownership'][row]
        progress_status = games_list['progress_status'][row]
        achievements1 = games_list['achievements1'][row]
        achievements2 = games_list['achievements2'][row]
        online_info = games_list['online_info'][row]
        progress_notes = games_list['progress_notes'][row]
        rating = games_list['rating'][row]
        review_comments = games_list['review_comments'][row]
        now_playing = games_list['now_playing'][row]
        whishlist = games_list['whishlist'][row]
        
        new_game = NewGameObj(driver)
        assert new_game.game_name_input

        new_game.add_new_game_detailed_mode_process(
            game_name, 
            compilation,
            str(system), 
            str(original_system), 
            str(region), 
            ownership,
            progress_status, 
            achievements1,
            achievements2,
            online_info,
            progress_notes, 
            rating,
            review_comments,
            now_playing,
            whishlist
            )
        print('\n')
        print(game_name, 'added to your Backloggery :D')
    
    # assert driver.find_element_by_css_selector("div .update-g"), 'Games added to your Backloggery :D'
