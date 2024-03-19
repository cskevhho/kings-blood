import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.polygon.com/final-fantasy-7-rebirth-ff7r-guide/24082221/queens-blood-cards-all-list-how-to-get'

# get page
response = requests.get(url)
response.raise_for_status()

# parse page?
soup = BeautifulSoup(response.text, 'html.parser')

# get table?
cards_table = soup.find('table')

# suck in card data 
cards = []
for row in cards_table.find('tbody').find_all('tr'):
    cols = row.find_all('td')
    card_details = {
        'number': cols[0].text.strip(),
        'name': cols[1].text.strip(),
        'stats': cols[2].text.strip(),
        'effect': cols[3].text.strip(),
        'location': cols[4].text.strip(),
        'how_to_get': cols[5].text.strip(),
    }
    cards.append(card_details)

# store into one json file???
with open('cards.json', 'w') as file:
    json.dump(cards, file, indent=4)

print(f'total:{len(cards)}/141')
