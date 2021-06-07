import requests
from bs4 import BeautifulSoup
import pandas as pd

pager = 1 
links = []

while pager <= 12:
    if pager == 1:
      url = "https://timesofindia.indiatimes.com/astrology/horoscope"
    else:
      url = "https://timesofindia.indiatimes.com/astrology/horoscope/" + str(pager)
    
    response= requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    
    for tag in soup.find_all('ul', {'class' : 'top-newslist'}):
         for anchor in tag.find_all('a'):
            links.append(anchor['href'])
    pager = pager + 1
    print(links)


df = pd.DataFrame({'col':links})
df.to_csv("D:/links.csv")

