#from datetime import datetime
from bs4 import BeautifulSoup
import requests
from csv import writer

##Set Global Variables
global table

##Get Current Time
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#
# now = datetime.now()
#
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute

##Web Scraping Beatiful Soup
current = requests.get('https://dbkpop.com/tag/comebacks')

january = requests.get('https://dbkpop.com/2019/12/02/january-2020-k-pop-comebacks-and-debuts')
february = requests.get('https://dbkpop.com/2019/12/26/february-2020-k-pop-comebacks-and-debuts')
march = requests.get('https://dbkpop.com/2020/01/23/march-2020-k-pop-comebacks-and-debuts')
april = requests.get('https://dbkpop.com/2020/02/04/april-2020-k-pop-comebacks-and-debuts')
may = requests.get('https://dbkpop.com/2020/04/03/may-2020-k-pop-comebacks-and-debuts')
june = requests.get('https://dbkpop.com/2020/04/20/june-2020-k-pop-comebacks-and-debuts')
july = requests.get('https://dbkpop.com/2020/05/11/july-2020-k-pop-comebacks-and-debuts')
august = current
september = current
october = current
november = current
december = current

def getMonth(month):
    Found = 0
    global paragraphString
    global returnedMonth

    if month == 1 or month == MONTHS[0]:
        response = requests.get('https://dbkpop.com/2019/12/02/january-2020-k-pop-comebacks-and-debuts')
        Found = 1
        returnedMonth = MONTHS[0]
    elif month == 2 or month == MONTHS[1]:
        response = requests.get('https://dbkpop.com/2019/12/26/february-2020-k-pop-comebacks-and-debuts')
        Found = 1
        returnedMonth = MONTHS[1]
    elif month == 3 or month == MONTHS[2]:
        response = requests.get('https://dbkpop.com/2020/01/23/march-2020-k-pop-comebacks-and-debuts')
        Found = 1
        returnedMonth = MONTHS[2]
    elif month == 4 or month == MONTHS[3]:
        response = requests.get('https://dbkpop.com/2020/02/04/april-2020-k-pop-comebacks-and-debuts')
        Found = 1
        returnedMonth = MONTHS[3]
    elif month == 5 or month == MONTHS[4]:
        response = requests.get('https://dbkpop.com/2020/04/03/may-2020-k-pop-comebacks-and-debuts')
        Found = 1
        returnedMonth = MONTHS[4]
    elif month == 6 or month == MONTHS[5]:
        response = requests.get('https://dbkpop.com/2020/04/20/june-2020-k-pop-comebacks-and-debuts')
        Found = 1
        returnedMonth = MONTHS[5]
    elif month == 7 or month == MONTHS[6]:
        response = requests.get('https://dbkpop.com/2020/05/11/july-2020-k-pop-comebacks-and-debuts')
        Found = 1
        returnedMonth = MONTHS[6]
    elif month == 8 or month == MONTHS[7]:
        response = current
        Found = 0
        returnedMonth = MONTHS[7]
    elif month == 9 or month == MONTHS[8]:
        response = current
        Found = 0
        returnedMonth = MONTHS[8]
    elif month == 10 or month == MONTHS[9]:
        response = current
        Found = 0
        returnedMonth = MONTHS[9]
    elif month == 11 or month == MONTHS[10]:
        response = current
        Found = 0
        returnedMonth = MONTHS[10]
    elif month == 12 or month == MONTHS[11]:
        response = current
        Found = 0
        returnedMonth = MONTHS[11]

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