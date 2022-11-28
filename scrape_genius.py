# Importing Packages
import lyricsgenius
import json, re, os

# Get Midnights from Spotify
genius = lyricsgenius.Genius('Bearer FjQostjLTcPJ4d4DZI6_ms4KrhA_wovfHJ2siG7rl1cUbHQ_2_Xl__4BGk_3-2Kv')
album = genius.search_album("Midnights (3am Edition)", "Taylor Swift")
# Save album as a json file
album.save_lyrics('data')
# Get the saved json file
album_json = json.load(open('data/Lyrics_Midnights3amEdition.json'))

# Create a file to write midnight lyrics
midnights = open('data/taylorswift_lyrics/10-midnights_3am_edition.csv','w')
midnights.write('album_name,track_title,track_n,lyric,line\n')

# Iterate through each track
for i in range(len(album_json['tracks'])):
    # Get title and lyrics
    title = album_json['tracks'][i]['song']['title']
    lyrics = album_json['tracks'][i]['song']['lyrics']

    # Remove things like [Chorus] and [Verse 1] etc.
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)

    # Remove all of the text before "Track Title Lyrics"
    lyrics = re.sub(f".*(?={title} Lyrics)", '', lyrics)

    # Remove the #Embed at the end of the string
    lyrics = re.sub("\d+Embed$", "", lyrics)

    # Turns the string into a list containing each line of the song
    lyrics = [s.strip() for s in lyrics.split('\n') if s]

    for line in range(len(lyrics)):
        # Write album name, track title, track number, lyric, and line to midnights file
        midnights.write("Midnights,%s,%i,%s,%i\n" % (title,i,lyrics[line],line+1))
