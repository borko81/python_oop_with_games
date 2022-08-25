from bs4 import BeautifulSoup as bs

css_soup = bs('<p class="body strikeout" id="my_id">Some text</p>', 'html.parser')
# get text
print(css_soup.p.string)
# get class of p tag
print(css_soup.p['class'])
# get id of p tag
print(css_soup.p['id'])