import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser

r = requests.get('https://www.imdb.com/title/tt0111161')

r.status_code
r.headers['Content-Type']
imdb = BeautifulSoup(r.text, 'html.parser')


title = imdb.select('title')

#Titulo
print(title)
#Numero Enlace
#print (len(urls_list))
#Lista Enlaces
#print(urls_list)
#Body
#print(body)