import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer
import re

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