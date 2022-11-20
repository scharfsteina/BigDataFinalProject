# Importing Packages
import pandas as pd
import numpy as np
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

# Merge all lyric lines together
genius_data = genius_data.drop('line', axis= 1)
genius_data = genius_data.groupby(['track_title', 'album_name'])['lyric'].apply(' '.join).reset_index()

# Save genius data to csv
genius_data.to_csv('data/genius.csv', index= True)

# Our merged datasets are now stored in spotify.csv and genius.csv
# and spotify_data and genius_data respectively
