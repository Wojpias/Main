import argparse
from Brewery import Brewery
import requests

# Setup argparse
parser = argparse.ArgumentParser(description="Get Breweries from a city")
parser.add_argument('--city', type=str, help='City to filter breweries')
args = parser.parse_args()

# Use argparse parameter to filter data from API
if args.city:
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_city={args.city}")
else:
    response = requests.get("https://api.openbrewerydb.org/breweries")

breweries_data = response.json()
breweries = [Brewery(data) for data in breweries_data[:20]]

for brewery in breweries:
    print(brewery)
