# Importing Packages
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Spotify API Info
album_uri = "3lS1y25WAhcqJDATJK70Mq"
client_id= "7037a3fd05ed4937bb639e43ecb77ed2" # ava's id
client_secret= "11282481d4c841839870004e083fc9a6" # ava's secret

# Spotipy Objects
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
tracks = sp.album_tracks(album_uri) #album_uri

# Constant Variables
album = "Midnights (3am Edition)"
artist = "Taylor Swift"
release_date = "2022-10-21"
album_size = len(tracks['items'])

# Track Data dictionary
track_data = {"name": [], "album": [album]*album_size, "artist": [artist]*album_size, "release_date":[release_date]*album_size, "length": [],"popularity": [], "danceability": [], "acousticness": [], "energy": [], "instrumentalness": [], "liveness": [], "loudness": [], "speechiness": [], "valence": [], "tempo": []}

# Function to add a feature and its value to track_data
def add_data(feature, value):
    if len(track_data[feature]) == 0:
        track_data[feature] = [value]
    else:
        track_data[feature].append(value)

# Iterate through each song in the album, add info to track_data
for n in range(album_size):
    id = tracks['items'][n]['id']
    features = sp.audio_features(id)
    add_data("name",tracks['items'][n]['name'])
    add_data("length", tracks['items'][n]['duration_ms'])
    add_data("popularity", (sp.track(id))['popularity'])
    features = (sp.audio_features(id))[0]
    for feature in features:
        if feature in track_data.keys(): # if relevant feature
            add_data(feature, features[feature])


midnight_spot = pd.DataFrame.from_dict(track_data)
# Saving the midnight spotify data so we don't have to scrape again
midnight_spot.to_csv('data/spotify_midnights.csv', index = True)

# merge midnights with all the other albums
other_albums = pd.read_csv('data/spotify_taylorswift.csv')
spotify = pd.concat([other_albums, midnight_spot], ignore_index = True)
spotify = spotify.drop(columns = ["index"])
spotify.to_csv('data/spotify.csv')
