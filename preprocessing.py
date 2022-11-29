# Importing Packages
import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer

# Load spotify data
spotify_data = pd.read_csv('data/spotify.csv')

# Load lyric data from kaggle dataset
# Combine genius lyrics datafiles together
lyrics_path = "data/taylorswift_lyrics"
albums = []
for album_csv in os.listdir(lyrics_path):
    album = pd.read_csv(f"{lyrics_path}/{album_csv}", on_bad_lines='skip')
    albums.append(album)
genius_data = pd.concat(albums, ignore_index = True)

# Merge lyric lines together from the same song
genius_data = genius_data.drop('line', axis= 1)
genius_data = genius_data.groupby(['track_title', 'album_name'])['lyric'].apply(' '.join).reset_index()

# Save genius data to csv
genius_data.to_csv('data/genius.csv', index= True)

# Load in billboard data
billboard_data = pd.read_csv('data/billboard.csv')

# Our merged datasets are now stored in spotify.csv, genius.csv, and billboard.csv
# and spotify_data, genius_data, and billboard_data respectively


# Stemming lyrics
porter = PorterStemmer()
genius_data['lyric_stemmed'] = ""
for i, song in enumerate(genius_data['lyric']):
    genius_data.loc[i, 'lyric_stemmed'] = " ".join([porter.stem(word) for word in song.split()])

# TFIDF Vectorization of lyrics
v = TfidfVectorizer(stop_words = 'english') # stop words?
x = v.fit_transform(genius_data['lyric_stemmed'])

tfidf_df = pd.DataFrame(x.toarray(), index = genius_data['track_title'], columns= v.get_feature_names_out())
tfidf_df.to_csv('data/tfidf_embedding.csv', index= True)
