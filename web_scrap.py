from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the page to scrape
url="https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

html_text = requests.get(url).text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_text, "html.parser")

# Find the table in the HTML

tables = soup.find_all("table")


tesla_table = None  # Initialize the variable

for table in tables:
    if "TSLA" in table.text:
        tesla_table = table
        break

if tesla_table:
    tesla_revenue = pd.read_html(str(tesla_table))[0]

    tesla_revenue.columns = ['Date', 'Revenue']
    tesla_revenue['Revenue'] = tesla_revenue['Revenue'].replace(r'[\$,]', '', regex=True)
    tesla_revenue['Revenue'] = tesla_revenue['Revenue'].replace('None', '')
    tesla_revenue.dropna(inplace=True)
    tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

    print(tesla_revenue.tail())
else:
    print("Tesla revenue table not found.")
