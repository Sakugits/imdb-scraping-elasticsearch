import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import numpy as np
import pandas as pd

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

def getSummaries(moviepage_link, storyline):
    r = requests.get(moviepage_link + '/plotsummary')
    r.status_code
    r.headers['Content-Type']
    imdbplot = BeautifulSoup(r.text, 'html.parser')
    content_ul = imdbplot.find('ul', attrs={'id' : 'plot-summaries-content'})
    list_summaries = content_ul.find_all('li')
    for summary in list_summaries:
        summaries.append(summary.p.text)

def getSynopsis(moviepage_link, synopsis):
    r = requests.get(moviepage_link + '/plotsummary')
    r.status_code
    r.headers['Content-Type']
    imdbplot = BeautifulSoup(r.text, 'html.parser')
    synopsis.append(imdbplot.find('ul', attrs={'id' : 'plot-synopsis-content'}).li.text)



def getMovieLinksFromExcel(path):
    movie_links = pd.read_excel(path, usecols="B").to_numpy()
    return movie_links



movie_links = getMovieLinksFromExcel("MovieGenreIGC_v3.xlsx")

for row in range (movie_links.shape[0] - 39930 ):
    r = requests.get(movie_links[row][0])

    r.status_code
    r.headers['Content-Type']
    imdb = BeautifulSoup(r.text, 'html.parser')
    print(imdb)
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
    getSynopsis(movie_links[row][0], synopsis)
    getSummaries(movie_links[row][0], summaries)
    getWriters(imdb, writers)
    getScore(imdb)
    getGenders(imdb, genders)
    getDirectors(imdb, directors)


    movie = {'Title' : title, 'Year' :  year, 'Genders' : genders, 'Score' : score, 'Directors' : directors, 'Writers' : writers, 'Synopsis' : synopsis, 'Summaries' : summaries}
    print (movie)









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

