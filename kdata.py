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
response = requests.get('https://dbkpop.com/2020/04/20/june-2020-k-pop-comebacks-and-debuts')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='site-main')

for post in posts:
    title = post.find(class_='entry-title').get_text()
    body = post.find(class_='entry-content clear')
    table = str(post.find(id='table_1'))
    # print(title)
    # print(body)
    # print(table)
paragraphs = body.find_all('p')

#Convert List of Elements to List of Text Only
n=0
paragraphList = []
paragraphString = ''
for n in range(len(paragraphs)):
    paragraphList.append(paragraphs[n].get_text() + '\n\n')
    n += 1
for n in range(len(paragraphList)):
    paragraphString += paragraphList[n]

##Test Web Scraping Site
#https://dbkpop.com/tag/comebacks