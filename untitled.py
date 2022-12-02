import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer
import re

merged = pd.read_csv('data/merged.csv')
billboard = pd.read_csv('data/billboard.csv')
billboard['taylors version'] = [1 if '(Taylor\'s Version)' in song else 0 for song in billboard['song']]
for i, song in enumerate(billboard['song']):
    billboard.loc[i, 'song'] = re.sub("|\-(.*)|[\(\[].*?[\)\]]",'', song).lower().strip()
print(billboard[billboard.duplicated(subset=['song'])])
billboard.to_csv('data/billboard1.csv')