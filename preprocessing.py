# Importing Packages
import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer
import re

# Load spotify data
spotify_data = pd.read_csv('data/spotify.csv', index_col = False) # CHANGE INDEX_COL = 0

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

for i, song in enumerate(genius_data['track_title']):
    # removing parentheses, brackets, dashes, and weird symbols from kaggle genius dataset, converting to lower case
    genius_data.loc[i, 'track_title'] = re.sub("|\-(.*)|[\(\[].*?[\)\]]",'', song).lower().replace('\u200b','')

# Save genius data to csv
genius_data.to_csv('data/genius.csv', index= True)

# Clean spotify data
for i, song in enumerate(spotify_data['name']):
    # removing parentheses, brackets, dashes, and weird symbols from kaggle genius dataset, converting to lower case
    spotify_data.loc[i, 'name'] = re.sub("|\-(.*)|[\(\[].*?[\)\]]",'', song).lower().replace('\u200b','')

spotify_data = spotify_data.drop([spotify_data.columns[0]], axis= 1)
#spotify_data.to_csv('data/spotify.csv', index= True) # update spotify csv file to cleaned version

# Merge spotify and genius data
temp = genius_data.copy()
temp = temp.rename(columns = {'track_title':'name', 'album_name':'album'})
merged = pd.merge(spotify_data,temp, on=['name','album'], how = 'inner')
merged.to_csv('data/merged.csv', index= True)

# Load in billboard data
billboard_data = pd.read_csv('data/billboard.csv')

# Our merged datasets are now stored in spotify.csv, genius.csv, and billboard.csv
# and spotify_data, genius_data, and billboard_data respectively

merged = pd.read_csv('data/merged.csv',index_col=False)
billboard = pd.read_csv('data/billboard.csv',index_col=False)
billboard['taylors version'] = [1 if '(Taylor\'s Version)' in song else 0 for song in billboard['song']] #create a column that marks a song as 1 or 0, depending on if it has Taylor's Version in the song title
for i, song in enumerate(billboard['song']):
    billboard.loc[i, 'song'] = re.sub("|\-(.*)|[\(\[].*?[\)\]]",'', song).lower().strip() #get rid of words in parantheses, lowercase the titles, and remove any spaces after
duplicated_songs = list(billboard[billboard.duplicated(subset=['song'])]['song']) # names of the songs that are duplicated


remove = [] #create a list of the index of songs to be removed
for i, row in billboard.iterrows():
    if row['song'] in duplicated_songs and row['taylors version'] == 0: 
        remove.append(i) #if songs are in the duplicated list and is also NOT Taylor's Version, add index to remove list


billboard = billboard.drop(billboard.index[remove]) #remove rows that are in the remove list
billboard = billboard.reset_index() 
billboard = billboard.drop([billboard.columns[0],billboard.columns[1],'taylors version'], axis= 1) #drop unnecessary columns
billboard.to_csv('data/billboard_cleaned.csv')
temp = billboard.copy()
temp = temp.rename(columns = {'song':'name'})
merged = pd.merge(merged,temp, on=['name'], how = 'left') #left merge dataset, with the merged dataset as the dataset to merge on to
merged['On Billboard'] = [0 if pd.isna(i) else 1 for i in merged['peak_position']]
merged = merged.drop(merged.columns[0], axis = 1) # removing unnamed column ????
merged.to_csv('data/fullymerged.csv')

# Stemming lyrics
porter = PorterStemmer()
merged['lyric_stemmed'] = ""
for i, song in enumerate(merged['lyric']):
    merged.loc[i, 'lyric_stemmed'] = " ".join([porter.stem(word) for word in song.split()])

# TFIDF Vectorization of lyrics
v = TfidfVectorizer(stop_words = 'english') # stop words?
x = v.fit_transform(merged['lyric_stemmed'])

tfidf_df = pd.DataFrame(x.toarray(), index = merged['name'], columns= v.get_feature_names_out())
tfidf_df.to_csv('data/tfidf_embedding.csv', index= True)
