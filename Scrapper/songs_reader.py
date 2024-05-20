import pandas as pd

def read_songs():
    data = pd.read_csv("C:\\Users\\Mawan\\PycharmProjects\\ContentGenerator\\Data\\songs.csv").columns
    return data