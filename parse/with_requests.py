import requests
from bs4 import BeautifulSoup as bs

import re

URL = 'https://abv.bg'

response = requests.get(URL)
if response.status_code == 200:
    soup = bs(response.text, 'html.parser')
    # print(soup.title.string)
    for row in soup.findAll('h3'):
        a_tag = row.findAll('a', href=True)
        urls = [a['href'] for a in a_tag if a['href'] != '#']
        for url in urls:
            r = requests.get(url)
            print(r.status_code)

    h3_or_h2 = soup.find_all(re.compile('^h2|3'))
    print(h3_or_h2)


