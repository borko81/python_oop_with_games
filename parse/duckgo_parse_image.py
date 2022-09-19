import requests
from bs4 import BeautifulSoup as bs


class Session:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
            }
        )

    @property
    def get_session(self):
        return self.session


class ParseImage:

    def __init__(self, name):
        self.what_search = name
        self.url = 'https://duckduckgo.com/'
        self.session = Session().get_session

    def get_data(self):
        params = (
            ('l', 'wt-wt'),
            ('q', self.what_search),
            ('f', ',,,'),
            ("engine", "duckduckgo"),
            ('iax', 'images'),
            ('ia', 'images'),
            ('p', '2')
        )
        data_from_url = self.session.get(self.url, params=params)

        if data_from_url.status_code == 200:
            soup = bs(data_from_url.text, 'html.parser')
            return soup
        return {'error': 'Error with comunication'}


if __name__ == '__main__':
    session = Session().get_session
    parse_url = ParseImage('кока кола')
    soup = parse_url.get_data()
    print(soup)
