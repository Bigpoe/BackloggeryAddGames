import pandas as pd
import warnings

class ExtractDataObj:

    def extract_data_from_csv(self):

        warnings.filterwarnings('ignore')
        
        # Extrasct as DataFrame
        df_games = pd.read_csv('./games_list.csv', encoding='utf-8', dtype=object)
        df_games['progress_status'].fillna(value='', inplace=True)
        df_games['progress_notes'].fillna(value='', inplace=True)

        return df_games
