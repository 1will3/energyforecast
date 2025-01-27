import yfinance as yf
import pandas as pd
from datetime import datetime

# Get data and save to CSV
def get_futures_data():
    try:
        # Download Crude Oil futures data
        print("Downloading Crude Oil futures data...")
        cl_data = yf.download("CL=F", 
                            start="2021-01-01", 
                            end="2024-12-31")
        
        # Download Natural Gas futures data
        print("Downloading Natural Gas futures data...")
        ng_data = yf.download("NG=F", 
                            start="2021-01-01", 
                            end="2024-12-31")
        
        # Add identifier columns
        cl_data['Product'] = 'Crude Oil'
        ng_data['Product'] = 'Natural Gas'
        
        # Create filenames with today's date
        today = datetime.now().strftime('%Y%m%d')
        cl_filename = f'crude_oil_futures_{today}.csv'
        ng_filename = f'natural_gas_futures_{today}.csv'
        
        # Save to CSV
        cl_data.to_csv(cl_filename)
        ng_data.to_csv(ng_filename)
        
        print(f"\nFiles saved as: \n{cl_filename}\n{ng_filename}")
        
        # Show some basic info about the data
        print("\nCrude Oil Data Shape:", cl_data.shape)
        print("Natural Gas Data Shape:", ng_data.shape)
        
        return cl_data, ng_data
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return None, None

# Run the function
cl_data, ng_data = get_futures_data()

# Show sample of the data if download successful
if cl_data is not None:
    print("\nCrude Oil Data Preview:")
    print(cl_data.head())