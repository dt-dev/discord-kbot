#from datetime import datetime
from bs4 import BeautifulSoup
import requests
from csv import writer

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

tables = soup.find_all(class_='wpDataTables wpDataTablesWrapper no-footer')

for table in tables:
    print(table)

##Test Web Scraping Site
#https://dbkpop.com/2020/04/20/june-2020-k-pop-comebacks-and-debuts