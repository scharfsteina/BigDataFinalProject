# Importing Packages
import requests
import re
from bs4 import BeautifulSoup

# scrape list of songs LATER
#midnights = 'http://api.genius.com/albums/Taylor-swift/Midnights-3am-edition'
#page = requests.get("https://genius.com/albums/Taylor-swift/Midnights-3am-edition")
#soup = BeautifulSoup(page.content, "html.parser")
#print(soup.body.routable-page)

midnights_songs = ["lavenderhaze", "maroon", "antihero", "snowonthebeach", "youreonyourownkid", "midnightrain", "question", "vigilanteshit", "bejeweled", "labyrinth", "karma", "sweetnothing", "mastermind", "thegreatwar", "paris", "highinfidelity", "glitch", "wouldvecouldveshouldve", "dearreader"]

# track_n = 0
# for song in midnights_songs:
#     url = f"https://www.azlyrics.com/lyrics/taylorswift/{song}.html"
#     soup = BeautifulSoup(requests.get(url).text, "html.parser").find('div', attrs={'class':'ringtone'})
#     song_name = soup.find_next('b').contents[0].strip()
#     lyrics = soup.find_next('div').text.strip()
#     with open("data/taylorswift_lyrics/10-midnights_3am_version.csv", "w") as w:
#         for line in lyrics.splitlines():
#             print(line + "hello")
#     w.close()
#
#     track_n += 1
