import requests
from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup as soup
import pandas as pd

url = 'https://www.billboard.com/artist/taylor-swift/chart-history/hsi/'

# Opening up connection, grabbing the page
uClient = uRequest(url)
page_html = uClient.read() # Offloads content into a variable
uClient.close() # Close the client

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Song titles
songs_html = page_soup.findAll('h3', id="title-of-a-story", class_="artist-chart-row-title")
songs = [i.get_text().strip() for i in songs_html]

# Debut date
debuts_html = page_soup.findAll('span', class_="artist-chart-row-debut-date")
debuts = [i.get_text().strip() for i in debuts_html]

# Peak position
peak_pos_html = page_soup.findAll('span', class_="artist-chart-row-peak-pos") #
peak_pos = [i.get_text().strip() for i in peak_pos_html]

# Peak date
peak_dates_html = page_soup.findAll('span', class_="artist-chart-row-peak-date") #
peak_dates = [i.get_text().strip() for i in peak_dates_html]

# Weeks on chart
weeks_html = page_soup.findAll('span', class_="artist-chart-row-week-on-chart") #
weeks = [i.get_text().strip() for i in weeks_html]

# Merge all data into one dataframe and save to csv
billboard_data = pd.DataFrame.from_dict({'song': songs, 'debut_date': debuts, 'peak_position': peak_pos, 'peak_date': peak_dates, 'weeks_on_chart': weeks})
billboard_data.to_csv('data/billboard.csv', index= True)
