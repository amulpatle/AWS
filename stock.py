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
    data_range = "P6K39c"
    percentage_change_class = "JwB6zf"
    # price_changed_class = "V53LMb"
    # price_changed_class = "JwB6zf"
    today_class = "enJeMd"
    
    r1 = 'ln0Gqe'
    # target_classes = ["P2Luy", "Ez2Ioe", "ZYVHBb"]
    
    
    current_price = float(soup.find(class_=class1).text.strip()[1:].replace(",",""))
    previous_price = float(soup.find(class_=class2).text.strip()[1:].replace(",",""))
    week_52_data = soup.find_all(class_=data_range)[2].text
    percentage_changed = soup.find_all(class_=percentage_change_class)
    # percentage_changed = soup.find(class_=price_changed_class)
    # price_change = soup.find(class_=price_changed_class).span
    # element = soup.find('div', class_=price_changed_class).text
    
    percentage_change = soup.find('span', class_='NydbP nZQ6l tnNmPe')
    
    
    target_element = soup.find('div', attrs={'jsname': 'zWwE1'})
    # today = soup.find(class_=today_class)


    # print(current_price)
    # print(previous_price)
    # print(week_52_data)
    
    
    # print(percentage_changed)
    # print(price_change)
    
    # print(element)
    # print(today_class)
    
    
    target_div = soup.find('div', jsname='CGyduf')

# Check if the target div is found
    if target_div:
        # Find the specific percentage change value
        percentage_change = target_div.find('div', class_='JwB6zf')
        if percentage_change:
            # Extract and print the text
            extracted_value = percentage_change.get_text(strip=True)
            print("Extracted Value:", extracted_value)  # Should output: 4.58%
        else:
            print("Percentage change value not found within the target div.")
    else:
        print("Target div with jsname='CGyduf' not found.")

scrape_stock_data("TSLA","NASDAQ")




