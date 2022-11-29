import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load data
spotify = pd.read_csv('data/spotify.csv')
genius = pd.read_csv('data/genius.csv')
#billboard = pd.read_csv('data/billboard.csv')
genius_tfidf = pd.read_csv('data/tfidf_embedding.csv')

# Function to get album
def get_album(song, spotify):
	return (spotify.loc[spotify.name == song,'album']).to_string(index=False)

tfidf_df = genius_tfidf.loc[:, genius_tfidf.columns != 'track_title']

# Elbow method to determine optimal number of clusters
def elbow():
	ss_dist = []
	K = range(2,15) # possible number of clusters
	for num_clusters in K :
		kmeans = KMeans(n_clusters=num_clusters)
		kmeans.fit(tfidf_df)
		ss_dist.append(kmeans.inertia_)
	plt.plot(K,ss_dist,'bx-')
	plt.xlabel("Values of K") 
	plt.ylabel("Sum of squared distances/Inertia") 
	plt.title("Elbow Method For Optimal k")
	plt.show(); # Shows that there is no optimal number of clusters

# For 10 clusters solution maybe the songs are aligned by albums
def cluster_kmeans(n):
	kmeans = KMeans(n_clusters=n)
	kmeans.fit(tfidf_df)
	clusters = kmeans.labels_
	pca = PCA(n_components=3, random_state=42)
	pca_vecs = pca.fit_transform(tfidf_df)
	x0 = pca_vecs[:, 0]
	x1 = pca_vecs[:, 1]
	print(pca.explained_variance_ratio_)
	genius['cluster'] = clusters
	genius['x0'] = x0
	genius['x1'] = x1

#albums = [get_album(song, spotify) for song in genius["track_title"]]
#print(albums)

cluster_kmeans(10)

#album_genius = [album for album in genius['album_name']]

#album_spotify = [album for album in spotify['album']]

#print(set(album_genius)^(set(album_spotify)))
# # set image size
plt.figure(figsize=(12, 7))
# set title
plt.title("Taylor Swift Lyrics TF-IDF + KMeans", fontdict={"fontsize": 18})
# set axes names
plt.xlabel("X0", fontdict={"fontsize": 16})
plt.ylabel("X1", fontdict={"fontsize": 16})
#  create scatter plot with seaborn, where hue is the class used to group the data
sns.scatterplot(data=genius, x='x0', y='x1', hue='cluster', palette="viridis")
plt.show()
