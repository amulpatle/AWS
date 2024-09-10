from bs4 import BeautifulSoup
import requests
import time

def scrape_stock_data(symbol,exchange):
    
    sym = ['NGS', 'NGM', 'NCM']
    
    if exchange in sym:
        exchange = 'NASDAQ'
    
    url = f'https://www.google.com/finance/quote/{symbol}:{exchange}'
    print("url =======================>>>>>>>>>>>>>>>>>>>>>",url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')

            class1 = "YMlKec fxKbKc"
            class2 = "P6K39c"
            class3 = "yf-tx3nkj"
            
            current_price = float(soup.find(class_=class1).text.strip()[1:].replace(",",""))
            previous_close = float(soup.find(class_=class2).text.strip()[1:].replace(",",""))
            print("current_price ==================>>>>>",current_price)
            print("previous_close ==================>>>>>",previous_close)
            stock_response = {
                'current_price':current_price,
                'previous_close':previous_close,
            }
            return stock_response
        else:
            return f'Error scraping the data for symbol {symbol}'
    except Exception as e:
        print(f'Error scraping the data:{e}')
        return None




