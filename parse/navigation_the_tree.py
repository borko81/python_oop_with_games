from bs4 import BeautifulSoup as bs
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="https://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs(html_doc, 'html.parser')
for a in soup.findAll('a'):
    href = a['href']
    if href.startswith('https'):
        print(href)

print(soup.body.b)

h = soup.head
# print(h.string)
# print(h.contents)
for t in h.children: print(t)

# for row in soup.descendants:
#     print(row)

# for s in soup.stripped_strings:
#     print(s.strip())

a = soup.find('a')
print('-' * 20)
print(a.parents)
print('-' * 20)
for tag in soup.find_all(re.compile('^a')):
    if tag.has_attr('class') and tag['class'][0] == 'sister':
        print(tag)

