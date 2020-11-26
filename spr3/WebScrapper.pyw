import requests
from bs4 import BeautifulSoup

result = requests.get("https://weather.com/news")
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
titles = []

for a in soup.find_all('a', href=True, class_="ListItem--listItem--1r7mf ListItem--disableBorder--Lfd0N CollectionMediaList--listItem--3XjSb Button--default--2yeqQ"):
	urls.append("https://weather.com" + a['href'])

for span in soup.find_all('span', class_="Ellipsis--ellipsis--lfjoB", style="-webkit-line-clamp:3"):
	titles.append(span.text)

i=0
while i!=len(urls):
	print(titles[i]+":\n"+urls[i]+"\n", file=open("news.txt", "a"))
	i+=1