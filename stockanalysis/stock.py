# from bs4 import BeautifulSoup
# import requests

# def f(symbol):
#     url = f"https://finance.yahoo.com/quote/{symbol}/"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content,'html.parser')
#     current_price = soup.find(f"fin-streamer",{"data-symbol":{symbol}})
#     # previous_close = soup.find('td',{'data-test'})
#     print(current_price)
    
# f('AAPL') 


# from bs4 import BeautifulSoup
# import requests

# def f(symbol):
#     url = f"https://finance.yahoo.com/quote/{symbol}/"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Find the fin-streamer tag with the correct data-symbol attribute
#     fin_streamer = soup.find('fin-streamer', {"data-symbol": symbol})
    
#     # Access the span tag inside the fin-streamer
#     if fin_streamer:
#         span_tag = fin_streamer.find('span')
#         print(fin_streamer)
#     else:
#         print("fin-streamer tag not found.")

# f('AAPL')

from bs4 import BeautifulSoup
import requests
import time

ticker = 'INFY'
url = f'https://www.google.com/finance/quote/{ticker}:NSE'

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
# print(soup)
class1 = "YMlKec fxKbKc"
class2 = "P6K39c"
class3 = "yf-tx3nkj"
current_price = float(soup.find(class_=class1).text.strip()[1:].replace(",",""))
previous_price = float(soup.find(class_=class2).text.strip()[1:].replace(",",""))

print(current_price)
print(previous_price)




