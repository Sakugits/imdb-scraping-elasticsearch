import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import numpy as np
import pandas as pd
import time
import json

#Function to get all the directors
def getDirectors(moviepage, directors):
    div_list_directors = moviepage.find('div', class_='sc-fa02f843-0 fjLeDR').div.ul
    list_director = div_list_directors.findAll('li')
    for director in list_director:
        directors.append(director.a.text)

def getTitle(moviepage):
    return moviepage.select_one('h1').text

def getGenders(movipage, genders):
    gender_data = movipage.find('div', attrs={'data-testid' : 'genres'})
    list_gender = gender_data.find_all('span')
    for gender in list_gender:
        genders.append(gender.text)

def getScore(moviepage):
    return float(moviepage.find('span', attrs={'class': 'sc-7ab21ed2-1 jGRxWM'}).text)

def getYear(moviepage):
    return int(moviepage.find('a', attrs={'class': 'ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh'}).text)
    

def getWriters(moviepage, writers):
    content_div = moviepage.find('div', class_='sc-fa02f843-0 fjLeDR')
    writers_div = content_div.findAll('div')
    #Note all tags are the same for all elemnts in directors and wrtiters so this is the only way to get the Writers, 
    writers_div.pop(0)
    writers_list_ul = writers_div[0].find('ul')
    writers_list = writers_list_ul.findAll('li')
    for writer in writers_list:
        writers.append(writer.a.text)

def getSummariesAndSynopsis(moviepage_link, synopsis, summaries):
    headers = {'Accept-Language': 'en-US,en;q=0.5', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(moviepage_link + '/plotsummary', headers=headers)
    r.status_code
    r.headers['Content-Type']
    imdbplot = BeautifulSoup(r.text, 'html.parser')
    content_ul = imdbplot.find('ul', attrs={'id' : 'plot-summaries-content'})
    list_summaries = content_ul.find_all('li')
    for summary in list_summaries:
        summaries.append(summary.p.text)
    if(imdbplot.find('ul', attrs={'id' : 'plot-synopsis-content'}).li.text == '\nIt looks like we don\'t have a Synopsis for this title yet. Be the first to contribute! Just click the "Edit page" button at the bottom of the page or learn more in the Synopsis submission guide.\n'):
           return
    else:
        synopsis.append(imdbplot.find('ul', attrs={'id' : 'plot-synopsis-content'}).li.text)
"""
def getSynopsis(moviepage_link, synopsis):
    r = requests.get(moviepage_link + '/plotsummary')
    r.status_code
    r.headers['Content-Type']
    imdbplot = BeautifulSoup(r.text, 'html.parser')
    synopsis.append(imdbplot.find('ul', attrs={'id' : 'plot-synopsis-content'}).li.text)
"""


def getMovieLinksFromExcel(path):
    movie_links = pd.read_excel(path, usecols="B").to_numpy()
    return movie_links

movie_links = getMovieLinksFromExcel("MovieGenreIGC_v3.xlsx")

movies = []
row = 0

while (row <= 39000): #Esto seria para un el total de peliculas: 39967
    try:
        if (row < 27519):
            headers = {'Accept-Language': 'en-US,en;q=0.5', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            r = requests.get(movie_links[row][0], headers=headers) #Esta linea es a la que me refiero, le ejecucion de esta linea demora 1.5 segundos (lo he medido)
            r.status_code
            r.headers['Content-Type']
            imdb = BeautifulSoup(r.text, 'html.parser')
        else:
            link = movie_links[row][0]
            idx = link.index('0')
            link = link[:idx] + link[idx+1:]
            r = requests.get(link, headers=headers)
            r.headers['Content-Type']
            imdb = BeautifulSoup(r.text, 'html.parser')
    except:
        continue
    directors = []
    writers = []
    genders = []
    summaries = []
    synopsis = []

    start_time = time.time()
    try:
        title = getTitle(imdb)
    except:
        title = None
    try:
        score = getScore(imdb)
    except:
        score = None
    try:
        year = getYear(imdb)
    except:
        year = None
    try:
        getGenders(imdb, genders)
    except:
        genders = []

    try:
        getDirectors(imdb, directors)
    except:
        directors = []

    getSummariesAndSynopsis(movie_links[row][0], synopsis, summaries)
    
    try:
        getWriters(imdb, writers)
    except:
        writers = []

    #print(title)
    #print(year)
    #print (summaries)
    #print (len(summaries))
    #print(synopsis)
    #print (len(synopsis))
    #print(title)
    #print(writers)
    #print(score)
    #print(genders)
    #print(directors)


    movie = {
        'title' : title,
        'year' :  year,
        'genders' : genders, 
        'score' : score, 
        'directors' : directors, 
        'writers' : writers, 
        'synopsis' : synopsis, 
        'summaries' : summaries
    }
    print (title)
    movies.append(movie)
    row += 3

j = json.dumps(movies, indent=4)
with open('movies.json', 'w') as f:
    f.write(j)
    f.close










#print(year)
#print((movie_links[1][0]))
#Titulo
#print (summaries)
#print (len(summaries))
#print(synopsis)
#print (len(synopsis))
#print(title)
#print(writers)
#print(score)
#print(genders)
#print(directors)

