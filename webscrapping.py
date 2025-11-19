from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

link = 'https://www.youtube.com/watch?v=gRLHr664tXA'
doc = BS(urlopen(link), 'lxml')

tag = doc.find("title")

print(tag)