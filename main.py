import requests
from bs4 import BeautifulSoup
import json


my_stocks = ['POLY.L', 'CGH.L', 'BTC-GBP']
stock_data = []


def getData(symbol):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    
    url = f'https://uk.finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'symbol': symbol,
        'price': soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
        'price_change':  soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text,
        'change': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text,
    }
    return stock


for item in my_stocks:
    stock_data.append(getData(item))
    print('Getting: ', item)

with open('stockdata.json', 'w') as f:
    json.dump(stock_data, f)

print('Fin')