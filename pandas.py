import requests
from bs4 import BeautifulSoup
import pandas as pd

url = ''
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

prices = soup.find_all('span', {'class': 'price'})

df = pd.DataFrame() #dataframe

for price in prices:
    text = price.text.strip()
    df = df.append({'price': text}, ignore_index=True)

df.to_csv('prices.csv', index=False)