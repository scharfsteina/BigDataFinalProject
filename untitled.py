import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer
import re

merged = pd.read_csv('data/merged.csv',index_col=False)
billboard = pd.read_csv('data/billboard.csv',index_col=False)
billboard['taylors version'] = [1 if '(Taylor\'s Version)' in song else 0 for song in billboard['song']]
for i, song in enumerate(billboard['song']):
    billboard.loc[i, 'song'] = re.sub("|\-(.*)|[\(\[].*?[\)\]]",'', song).lower().strip()
duplicated_songs = list(billboard[billboard.duplicated(subset=['song'])]['song']) # names of the songs that are duplicated
#billboard = billboard.loc[(billboard['song'] not in duplicated_songs) or (billboard['taylors version'] != 0)]


remove = []
for i, row in billboard.iterrows():
    if row['song'] in duplicated_songs and row['taylors version'] == 0: 
        remove.append(i)

billboard = billboard.drop(billboard.index[remove])
billboard = billboard.reset_index()
billboard = billboard.drop([billboard.columns[0],billboard.columns[1],'taylors version'], axis= 1)
#billboard.to_csv('data/billboard_cleaned.csv')
temp = billboard.copy()
temp = temp.rename(columns = {'song':'name'})
merged = pd.merge(merged,temp, on=['name'], how = 'left')
merged.to_csv('data/fullymerged.csv')