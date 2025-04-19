import yfinance as yf
import pandas as pd

tesla_data = yf.download('TSLA')

# Reset the index so 'Date' becomes a column
tesla_data.reset_index(inplace=True)

# Display the first 5 rows
print(tesla_data.head())