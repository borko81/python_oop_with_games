import requests
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen

params = {
    "q": "pexels cat",
    "tbm": "isch",
    "hl": "bg"
}
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get("https://www.google.com/search", params=params, headers=headers)
soup = bs(html.text, 'html.parser')

for google_image in soup.findAll('isv-r'):
    print(google_image)
