import requests

class Brewery:
    def __init__(self, data):
        # Przykładowe atrybuty, należy dostosować do danych z API
        self.name = data['name']
        self.type = data['brewery_type']
        # ... inne atrybuty ...

    def __str__(self):
        return f"Brewery: {self.name}, Type: {self.type}"

# Użycie klasy po pobraniu danych z API
response = requests.get("https://api.openbrewerydb.org/breweries")
breweries_data = response.json()

breweries = [Brewery(data) for data in breweries_data[:20]]
for brewery in breweries:
    print(brewery)
