import requests
from bs4 import BeautifulSoup as bs
import re, json
import csv
import pandas as pd 

with open('links indian express.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        links = {rows[0]:rows[1] for rows in reader}
        
zodiac = []
horoscope = []
dates = []
x = 0
signs = ['ARIES', 'TAURUS', 'GEMINI', 'CANCER', 'LEO', 'VIRGO', 'LIBRA', 'SCORPIO', 'SAGITTARIUS', 'CAPRICORN', 'AQUARIUS', 'PISCES']

while x < 3:
    url = links[str(x)]
    r = requests.get(url, headers = {'User-Agent':'Mozilla/5.0'})
    response= requests.get(url)
    soup = bs(response.content,"html.parser")
    data = json.loads(re.search(r'(\{"@context.*articleBody.*\})', r.text).group(1))
    date = json.loads(re.search(r'(\{"@context.*datePublished.*\})', r.text).group(1))
    date = date['datePublished']
    dates.append(date)
   # print(data['articleBody'])
        
    for number, sign in enumerate(signs):
      
        if number < 11:
            # print(re.search(f'({sign}.*?){signs[number + 1]}', data['articleBody']).group(1))
            t = re.search(f'({sign}.*?){signs[number + 1]}', data['articleBody']).group(1)
            t = re.sub("\\s*\\([^\\)]+\\)", "", t)
            t = re.sub(f'({sign}.*?)', "", t)
            horoscope.append(t)
            zodiac.append(signs[number])
       # else:
            # print(re.search(f'({sign}.*)', data['articleBody']).group(1))
       
    
    print("Scraped Link #" + str(x))
    x = x + 1
    
data = {'Signs': zodiac, 'Horoscope': horoscope}
df = pd.DataFrame(data)

df.to_csv("indian express.csv")
