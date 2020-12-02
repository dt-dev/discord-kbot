#from datetime import datetime
from bs4 import BeautifulSoup
import requests
from csv import writer

global paragraphString
global table

##Get Current Time
# MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#
# now = datetime.now()
#
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute

##Web Scraping Beatiful Soup
currentResponse = requests.get('https://dbkpop.com/2020/11/05/december-2020-k-pop-comebacks-and-debuts')

currentSoup = BeautifulSoup(currentResponse.text, 'html.parser')

currentPosts = currentSoup.find_all(class_='site-main')

for currentPost in currentPosts:
    title = currentPost.find(class_='entry-title').get_text()
    body = currentPost.find(class_='entry-content clear')
    table = str(currentPost.find(id='table_1'))
    # print(title)
    # print(body)
    # print(table)
paragraphs = body.find_all('p')

#Convert List of Elements to List of Text Only
n=0
currentParagraphList = []
currentParagraphString = ''
for n in range(len(paragraphs)):
    currentParagraphList.append(paragraphs[n].get_text() + '\n\n')
    n += 1
for n in range(len(currentParagraphList)):
    currentParagraphString += currentParagraphList[n]
currentParagraphString = currentParagraphString[0:2047]

##Web Scraping Beatiful Soup
nextResponse = requests.get('https://dbkpop.com/2020/12/03/january-2021-k-pop-comebacks-and-debuts')

nextSoup = BeautifulSoup(nextResponse.text, 'html.parser')

nextPosts = nextSoup.find_all(class_='site-main')

for nextPost in nextPosts:
    title = nextPost.find(class_='entry-title').get_text()
    body = nextPost.find(class_='entry-content clear')
    table = str(nextPost.find(id='table_1'))
    # print(title)
    # print(body)
    # print(table)
paragraphs = body.find_all('p')

#Convert List of Elements to List of Text Only
n=0
nextParagraphList = []
nextParagraphString = ''
for n in range(len(paragraphs)):
    nextParagraphList.append(paragraphs[n].get_text() + '\n\n')
    n += 1
for n in range(len(nextParagraphList)):
    nextParagraphString += nextParagraphList[n]
nextParagraphString = nextParagraphString[0:2047]

##Tables of All Artists
table = requests.get('https://dbkpop.com/db/all-k-pop-idols')

tableSoup = BeautifulSoup(table.text, 'html.parser')

table = tableSoup.table

table_rows = table.find_all('tr')

stageNameList = []
fullNameList = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    if len(row) >= 1:
        stageNameList.append(row[1])
        fullNameList.append(row[2])

##Subscriptions
subcriptions = open('subscriptions.txt', 'r+')


##Test Web Scraping Site
#https://dbkpop.com/tag/comebacks