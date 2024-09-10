from bs4 import BeautifulSoup
import requests
import time

def scrape_stock_data(symbol,exchange):
    
    url = f'https://www.google.com/finance/quote/{symbol}:{exchange}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    class1 = "YMlKec fxKbKc"
    class2 = "P6K39c"
    class3 = "yf-tx3nkj"
    
    current_price = float(soup.find(class_=class1).text.strip()[1:].replace(",",""))
    previous_price = float(soup.find(class_=class2).text.strip()[1:].replace(",",""))

    print(current_price)
    print(previous_price)




