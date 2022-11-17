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

def getYear(moviepage):
    year.append(moviepage.find('a', attrs={'class': 'ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh'}).text)
    

def getWriters(moviepage, writers):
    content_div = moviepage.find('div', class_='sc-fa02f843-0 fjLeDR')
    writers_div = content_div.findAll('div')
    #Note all tags are the same for all elemnts in directors and wrtiters so this is the only way to get the Writers, 
    writers_div.pop(0)
    writers_list_ul = writers_div[0].find('ul')
    writers_list = writers_list_ul.findAll('li')
    for writer in writers_list:
        writers.append(writer.a.text)

def getSummaries(moviepage, storyline):
    r = requests.get('http://www.imdb.com/title/tt2077826/plotsummary')
    r.status_code
    r.headers['Content-Type']
    imdbplot = BeautifulSoup(r.text, 'html.parser')
    content_ul = imdbplot.find('ul', attrs={'id' : 'plot-summaries-content'})
    list_summaries = content_ul.find_all('li')
    for summary in list_summaries:
        summaries.append(summary.p.text)

def getSynopsis(moviepage, synopsis):
    r = requests.get('http://www.imdb.com/title/tt2077826/plotsummary')
    r.status_code
    r.headers['Content-Type']
    imdbplot = BeautifulSoup(r.text, 'html.parser')
    synopsis.append(imdbplot.find('ul', attrs={'id' : 'plot-synopsis-content'}).li.text)




r = requests.get('http://www.imdb.com/title/tt2077826/')

r.status_code
r.headers['Content-Type']
imdb = BeautifulSoup(r.text, 'html.parser')
directors = []
writers = []
genders = []
title = []
score = []
summaries = []
synopsis = []
year = []

getTitle(imdb)
getYear(imdb)
getSynopsis('https://www.imdb.com/title/tt3703750/', synopsis)
getSummaries('https://www.imdb.com/title/tt3703750/', summaries)
getWriters(imdb, writers)
getScore(imdb)
getGenders(imdb, genders)
getDirectors(imdb, directors)






print(year)
#Titulo
print (summaries)
print (len(summaries))
print(synopsis)
print (len(synopsis))
print(title)
print(writers)
print(score)
print(genders)
print(directors)

