# Importing Packages
import numpy as np
import pandas as pd
import os

# Load spotify data
spotify_data = pd.read_csv('data/spotify_taylorswift.csv')

# Load lyric data from kaggle dataset
lyrics_path = "data/taylorswift_lyrics"
for album_csv in os.listdir(lyrics_path):
    album = pd.read_csv(f"{lyrics_path}/{album_csv}")
    print(album.columns)
