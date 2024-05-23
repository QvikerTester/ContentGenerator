import pandas as pd
from Scrapper import Data
def read_songs():
    data = pd.read_csv("C:\\Users\\Mawan\\PycharmProjects\\ContentGenerator\\Data\\songs.csv").columns
    return data
def add_song_title(used_songs):
    data = pd.read_csv(Data.USED_TITLE)
    data.at[0, len(data.columns)+1] = used_songs
    print(used_songs)
    data.to_csv(Data.USED_TITLE, index=False)

def duplicate_remover(song):
    df = pd.read_csv(Data.USED_TITLE)
    df_list = df.values.tolist()[0]
    if song in df_list:
        return True

