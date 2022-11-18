import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict
import pandas as pd

album_uri= "3lS1y25WAhcqJDATJK70Mq"

client_id= "e1400899c4704525acbcc2f6088ed672"
client_secret= "0d4b5d9d7dc341f3a0c0d4f33ab9f7ba"

midnight= defaultdict(list)

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print("problem before calling")
tracks = sp.album_tracks(album_uri)

print("problem after calling")
for n in range(len(tracks['items'])):
    album= "Midnights (3am Edition)"
    artist= "Taylor Swift"
    release_date= "2022-10-21"
    name= tracks['items'][n]['name']
    id= tracks['items'][n]['id']
    length= tracks['items'][n]['duration_ms']
    pop= sp.track(id)
    popularity= pop['popularity']
    features= sp.audio_features(id)
    danceability= features[0]['danceability']
    acousticness= features[0]['acousticness']
    energy= features[0]['energy']
    instrumentalness= features[0]['instrumentalness']
    liveness= features[0]['liveness']
    loudness= features[0]['loudness']
    speechiness= features[0]['speechiness']
    valence= features[0]['valence']
    tempo= features[0]['tempo']
    midnight[name].append(album)
    midnight[name].append(artist)
    midnight[name].append(release_date)
    midnight[name].append(length)
    midnight[name].append(popularity)
    midnight[name].append(danceability)
    midnight[name].append(acousticness)
    midnight[name].append(energy)
    midnight[name].append(instrumentalness)
    midnight[name].append(liveness)
    midnight[name].append(loudness)
    midnight[name].append(speechiness)
    midnight[name].append(valence)
    midnight[name].append(tempo)
    
column_names= ['album', 'artist', 'release_data', 'length', 'popularity', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'valence', 'tempo']
print('reached here')
midnight_spot= pd.DataFrame.from_dict(midnight, orient= 'index', columns= column_names)
midnight_spot.index.name= 'name'
midnight_spot.set_index('')

midnight_spot.to_csv('midnight_spotify.csv', index= True)
#print(tracks['items'][0][''])
