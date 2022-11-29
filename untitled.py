import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer

genius_data = pd.read_csv('data/genius.csv')

# Stemming lyrics
porter = PorterStemmer()
genius_data['lyric_stemmed'] = ""
for i, song in enumerate(genius_data['lyric']):
    genius_data.loc[i, 'lyric_stemmed'] = " ".join([porter.stem(word) for word in song.split()])

# TFIDF Vectorization of lyrics
v = TfidfVectorizer() # stop words?
x = v.fit_transform(genius_data['lyric_stemmed'])

tfidf_df = pd.DataFrame(x.toarray(), index = genius_data['track_title'], columns= v.get_feature_names_out())
tfidf_df.to_csv('data/tfidf_embedding.csv', index= True)