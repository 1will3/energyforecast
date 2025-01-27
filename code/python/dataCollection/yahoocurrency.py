import yfinance as yf
from datetime import datetime

def get_all_currency_data():
    print("Starting currency data download...")
    
    # Define all currency pairs we need
    currencies = {
        'DXY': 'DX-Y.NYB',      # US Dollar Index
        'EUR/USD': 'EURUSD=X',   # Euro
        'CAD/USD': 'CADUSD=X',   # Canadian Dollar
        'NOK/USD': 'NOKUSD=X',   # Norwegian Krone 
        'RUB/USD': 'RUBUSD=X'    # Russian Ruble
    }
    
    for name, ticker in currencies.items():
        print(f"\nDownloading {name} data using ticker: {ticker}")
        data = yf.download(ticker, 
                          start="2021-01-01", 
                          end="2024-01-14")
        
        # Save each currency's data
        filename = f'currency_{name.replace("/", "_")}_{datetime.now().strftime("%Y%m%d")}.csv'
        data.to_csv(filename)
        print(f"Saved {filename}")
        print(f"Data Shape: {data.shape}")
        print("First few rows:")
        print(data.head())

# Run the function
get_all_currency_data()