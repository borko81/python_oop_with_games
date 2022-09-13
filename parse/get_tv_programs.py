import requests
from bs4 import BeautifulSoup as bs
import asyncio

URLS = [
    'https://www.тв-програма.bg/tv/btv/',
    'https://www.тв-програма.bg/tv/fox-life/',
    'https://www.тв-програма.bg/tv/btv-action/',
    'https://www.тв-програма.bg/tv/diema/',
    'https://www.тв-програма.bg/tv/btv-comedy/',
    'https://www.тв-програма.bg/tv/hbo/',
    'https://www.тв-програма.bg/tv/hbo-comedy/',
    'https://www.тв-програма.bg/tv/hbo-3/'

]


class ShowTime:

    def __init__(self, url):
        self.url = url
        self.hours = []
        self.shows = []

    async def return_network_data(self):
        data = requests.get(self.url)
        soup = bs(data.text, 'html.parser')
        return soup

    async def read_result(self):
        table = await self.return_network_data()
        table_all = table.find('table', {'class': 'programTable'})

        for row in table_all.find_all('tr', {'class': ['light', 'dark']}):
            if len(row['class']) != 1:
                continue
            self.hours.append(
                row.find('td', {'class': 'timeHolder'}).find('div', {'class': 'programTime'}).text.strip())
            self.shows.append(row.find('a').text.strip())

    def __repr__(self):
        return "\n".join([f"{show_time} - {show_name}" for show_time, show_name in zip(self.hours, self.shows)])


async def show_me_result(url):
    btv = ShowTime(url)
    await btv.read_result()
    print(f"{'-' * 20} {url.split('/')[-2].upper()} {'-' * 20}")
    print(btv)


async def main():
    res = await asyncio.gather(*(show_me_result(i) for i in URLS))
    return res


if __name__ == '__main__':
    asyncio.run(main())
