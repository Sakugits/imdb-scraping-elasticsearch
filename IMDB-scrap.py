import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser

#Function to get all the directors
def getDirectors(moviepage, directors):
    div_list_directors = moviepage.find('div', class_='sc-fa02f843-0 fjLeDR').div.ul
    list_director = div_list_directors.findAll('li')
    for director in list_director:
        directors.append(director.a.text)

def getTitle(moviepage):
    title.append(moviepage.select_one('h1').text)

def getGenders(movipage, genders):
    gender_data = movipage.find('div', attrs={'data-testid' : 'genres'})
    list_gender = gender_data.find_all('span')
    for gender in list_gender:
        genders.append(gender.text)

def getScore(moviepage):
    score.append(moviepage.find('span', attrs={'class': 'sc-7ab21ed2-1 jGRxWM'}).text)
    

def getWriters(moviepage, writers):
    content_div = moviepage.find('div', class_='sc-fa02f843-0 fjLeDR')
    writers_div = content_div.findAll('div')
    #Note all tags are the same for all elemnts in directors and wrtiters so this is the only way to get the Writers, 
    writers_div.pop(0)
    writers_list_ul = writers_div[0].find('ul')
    writers_list = writers_list_ul.findAll('li')
    for writer in writers_list:
        writers.append(writer.a.text)



r = requests.get('https://www.imdb.com/title/tt3703750/')

r.status_code
r.headers['Content-Type']
imdb = BeautifulSoup(r.text, 'html.parser')
directors = []
writers = []
genders = []
title = []
score = []
storyline = []

getTitle(imdb)
gender = imdb.find_all('storyline-genres')
poster = imdb.find('div', class_='ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img').img
aux_guion = imdb.find('div', class_='sc-fa02f843-0 fjLeDR')
guion = aux_guion.select('a', class_='ipc-metadata-list-item__list-content-item')
content_div_sto = imdb.select('section', attrs={'data-testid' :'Storyline'})
trythis = imdb.findAll("div", class_="sc-132205f7-0 bJEfgD")
print(trythis)
print(content_div_sto)
getWriters(imdb, writers)
getScore(imdb)
getGenders(imdb, genders)
getDirectors(imdb, directors)




#Titulo
print(title)
print(storyline)
print(writers)
print(score)
print(genders)
print(directors)

