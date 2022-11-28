import pandas as pd
import seaborn as sb
from sklearn.cluster import KMeans

# Load data
spotify = pd.read_csv('data/spotify.csv')
#genius = pd.read_csv('data/genius.csv')
#billboard = pd.read_csv('data/billboard.csv')
genius_tfidf = pd.read_csv('data/tfidf_embedding.csv')




def get_album(song, spotify):
	return spotify.loc[spotify['name']==song,'album']

