import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict
import pandas as pd

album_uri= "3lS1y25WAhcqJDATJK70Mq"

client_id= "e1400899c4704525acbcc2f6088ed672"
client_secret= "0d4b5d9d7dc341f3a0c0d4f33ab9f7ba"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

tracks = sp.album_tracks(album_uri)

for n in range(len(tracks['items'])):
    song_name= tracks['items'][n]['name']
    id= tracks['items'][n]['id']
    length= tracks['items'][n]['duration_ms']
    features= sp.audio_features(id)
    acousticness= features[0]['acousticness']
    print(song_name, acousticness, length)

#print(tracks['items'][0][''])
