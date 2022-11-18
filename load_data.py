# Importing Packages
import numpy as np
import pandas as pd
import os

# Load spotify data
spotify_data = pd.read_csv('data/spotify.csv')

# Load lyric data from kaggle dataset
lyrics_path = "data/taylorswift_lyrics"
albums = []
for album_csv in os.listdir(lyrics_path):
    album = pd.read_csv(f"{lyrics_path}/{album_csv}", on_bad_lines='skip')
    albums.append(album)
genius_data = pd.concat(albums, ignore_index = True)
genius_data.to_csv("data/genius.csv")
