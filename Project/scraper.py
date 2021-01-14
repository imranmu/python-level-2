import csv
from typing import Dict, List, Any, Union

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations"

# Dictionary of HTTP headers
headers = {'User-Agent': f'Imran (ikbangesh@gmail.com)'}
response = requests.get(URL, headers=headers)

assert response.status_code == 200
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

table = soup.find('table', class_='wikitable')
print(table.caption)
rows = table.find_all('tr')
countries = []
date_joined = []
country_dicts = []
for row in rows:
    columns = row.find_all('td')
    if len(columns) > 0:
        name_col = columns[0]
        name = name_col.find_all('a')[1].string
        countries.append(name)

    #    date_col = columns[1] ## this does not work. Look for video to see how teacher did
    #    date_joined = date_col.string

        country_dict = {
            'Name': name,
            'Date Joined': date_joined
        }
        country_dicts.append(country_dict)
print(country_dicts)

with open('countries.csv', 'w') as file:
    writer = csv.DicWriter(file, ('Name', 'Date joined'))
    writer.writeheader()
    writer.writerows(country_dicts)
