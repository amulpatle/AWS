import requests
import pandas as pd

def fetch_nse_stock_list():
    # URL to fetch the NSE stock list in JSON format
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }
    
    try:
        # Initialize a session
        session = requests.Session()
        session.headers.update(headers)
        
        # Fetching the data from the URL
        response = session.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parsing the JSON data
        data = response.json()
        
        # Extract the stock data from the JSON response
        stocks = data.get('data', [])
        
        # Create a list to store formatted stock data
        stock_list = []
        for stock in stocks:
            stock_entry = {
                "name": stock.get("symbol", ""),  # Assuming the 'symbol' field contains the name
                "symbol": stock.get("symbol", ""),
                "sector": "",  # Sector information is not available in the current API response
                "exchange": "NSE",
                "country": "India"
            }
            stock_list.append(stock_entry)
        
        # Convert the list of dictionaries to a pandas DataFrame
        df = pd.DataFrame(stock_list, columns=["name", "symbol", "sector", "exchange", "country"])
        
        # Save the DataFrame to a CSV file
        df.to_csv('nse_stock_list.csv', index=False)
        print("Stock list saved to 'nse_stock_list.csv'.")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")

# Run the function
fetch_nse_stock_list()
