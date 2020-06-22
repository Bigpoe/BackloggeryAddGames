import pandas as pd
import warnings

class ExtractDataObj:

    def extract_simple_data_from_csv(self):
        warnings.filterwarnings('ignore')
        # Extrasct data and save it as DataFrame
        df_games = pd.read_csv('backloggery_add_games/utils/games_list_simple.csv', encoding='utf-8', dtype=str)
        df_games['progress_status'].fillna(value='', inplace=True)
        df_games['progress_notes'].fillna(value='', inplace=True)
        df_games['now_playing'].fillna(value='', inplace=True)
        df_games['whishlist'].fillna(value='', inplace=True)

        return df_games

    def extract_detailed_data_from_csv(self):
        warnings.filterwarnings('ignore')
        # Extrasct data and save it as DataFrame
        df_games = pd.read_csv('backloggery_add_games/utils/games_list_detailed.csv', encoding='utf-8', dtype=object)
        df_games['progress_status'].fillna(value='', inplace=True)
        df_games['progress_notes'].fillna(value='', inplace=True)
        df_games['now_playing'].fillna(value='', inplace=True)
        df_games['whishlist'].fillna(value='', inplace=True)

        return df_games
