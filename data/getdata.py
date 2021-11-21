from os import name
from bs4 import BeautifulSoup

html = open('favorites.html', 'r', encoding='utf-8')
bs = BeautifulSoup(html,"html.parser")

marks = bs.find_all('a')[:50]
content = []
# for i in range(len(marks)):
for i in range(50):
  content.append(
    { 'name': marks[i].string, 'icon': marks[i].get('icon'), 'url': marks[i].get('href')}
  )

print(content)