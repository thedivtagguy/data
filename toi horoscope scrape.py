import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import csv

with open('D:/links.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        links = {rows[0]:rows[1] for rows in reader}

x = 0
signs = []
horoscope = []
dates = []
while x < len(links):         
    url = links[str(x)]
    page = "https://timesofindia.indiatimes.com" + url
    response= requests.get(page)
    websoup = soup(response.content,"html.parser")
    
    for i in websoup.find_all('div', {'class', '_3Mkg- byline'}):
        date = i.text
        date = date.replace("Samir Jain |", "")
        j = 1
        while j <= 12: 
          dates.append(date)
          j = j + 1
    
    for anchor in websoup.find_all('span', {'class' : 'strong'}):
        signs.append(anchor.text)
        horoscope.append(anchor.next_sibling.next_sibling)
    print("Scraped link #" + str(x))
    x = x +1 
    
data = {'Date': dates, 'Signs': signs, 'Horoscope': horoscope}
df = pd.DataFrame(data)

df.to_csv("D:/scrape.csv")

