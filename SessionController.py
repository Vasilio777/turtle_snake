from constants import screensize, sessions_data
import pandas as pd

df = pd.read_csv(sessions_data)

class SessionController():
    def read_highscore():
        return max(df['score'].values)

    def write_session(score):
        global df
        
        last_session = int(df['session'].values[-1])
        new_score = pd.DataFrame({'session': [last_session+1], 'score': [score]})

        df = pd.concat([df, new_score], ignore_index=True)
        df.to_csv(sessions_data, index=False) 
