from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_stock_data(symbol,exchange):
    
    driver = webdriver.Chrome()
   

    # Open the webpage (replace with your actual URL containing the data)
    li = ['NGM','NCM','NMS']
    if exchange in li:
        url = f"https://www.google.com/finance/quote/{symbol}:NASDAQ"
        
        print("url ================>>>>>>>>>>>>>>>>",url)
    elif exchange == 'NSE':
        symbol = symbol+'.NS'
        url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'

    driver.get(url)

    try:
        # Percentage change
        # percentage_change_div = driver.find_element(By.CSS_SELECTOR, 'div[jsname="CGyduf"]')
        # percentage_change = percentage_change_div.find_element(By.CSS_SELECTOR, '.JwB6zf').text
        # print(percentage_change)
        
        parent_element = driver.find_element(By.CSS_SELECTOR, '[jsname="CGyduf"]')
        try:
            percentage_change_element = parent_element.find_element(By.CSS_SELECTOR, '.NydbP.nZQ6l.tnNmPe .JwB6zf')
            percentage_changed = percentage_change_element.text
        except:
            percentage_change_element = parent_element.find_element(By.CSS_SELECTOR, '.NydbP.VOXKNe.tnNmPe .JwB6zf')
            percentage_changed = percentage_change_element.text
            
        print(percentage_changed)
            
        # Today change
        target_div = driver.find_element(By.CSS_SELECTOR, 'div[jsname="CGyduf"]')
        try:
            
            price_changed = target_div.find_element(By.CSS_SELECTOR, '.P2Luy.Ez2Ioe.ZYVHBb').text
        except:
            price_changed = target_div.find_element(By.CSS_SELECTOR, '.P2Luy.Ebnabc.ZYVHBb').text
            
        print(price_changed)

        # Current Price
        price_div = driver.find_element(By.CSS_SELECTOR, 'div[jsname="AS5Pxb"]')
        current_price = price_div.find_element(By.CSS_SELECTOR, '.YMlKec').text
        print(current_price)
            
        # Previous Close
        previous_close_div = driver.find_element(By.XPATH, '//div[@class="gyFHrc"][1]//div[@class="P6K39c"]')
        previous_close = previous_close_div.text
        # print("Previous Close:", previous_close_value)  

        # Year Range
        year_range_div = driver.find_element(By.XPATH, '//div[@class="gyFHrc"][2]//div[@class="P6K39c"]')
        year_range_value = year_range_div.text
        week_52_low,week_52_high = year_range_value.split(' - ')
        print('low=>',week_52_low)
        print('hihg=>',week_52_high)
        
        
        # cap
        market_cap = driver.find_element(By.XPATH, '//div[@class="gyFHrc"][4]//div[@class="P6K39c"]').text
        # value = value_element.text
        print("Market Cap:", market_cap)
        
        # PE Ratio
        pe_ratio = driver.find_element(By.XPATH, '//div[@class="gyFHrc"][6]//div[@class="P6K39c"]').text
        # value = value_element.text
        print("pe_ratio:", pe_ratio)
        
        # Dividend & Yeild
        dividend_yield = driver.find_element(By.XPATH, '//div[@class="gyFHrc"][7]//div[@class="P6K39c"]').text
        print(dividend_yield)
        
        stock_response = {
            'current_price':current_price,
            'previous_close':previous_close,
            'price_changed':price_changed,
            'percentage_changed':percentage_changed,
            'week_52_low':week_52_low,
            'week_52_high':week_52_high,
            'market_cap':market_cap,
            'pe_ratio':pe_ratio,
            'dividend_yield':dividend_yield
            
        }
        return stock_response

            
    except Exception as e:
        print("Error:", str(e))

    finally:
        # Close the WebDriver
        driver.quit()

# scrape_stock_data('TSLA','NGM')



