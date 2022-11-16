
import re, requests
from bs4 import BeautifulSoup

URL = 'https://genius.com/Andy-shauf-the-magician-lyrics'
page = requests.get(URL)
html = BeautifulSoup(page.text, "html.parser")
lyrics = html.find('div[class^="SongPage__Section"]').get_text().encode('ascii','ignore')
