
# Extract all bird species from the website url https://xeno-canto.org
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import csv
import os

html = urlopen("https://xeno-canto.org/collection/species/all")
bs = BeautifulSoup(html, 'html.parser')

birdTable = bs.find('table', {'class': 'results'})
birds = birdTable.find_all('tr')

directory = os.getcwd()
filePath = os.path.join(directory, 'birdSpecies.csv')

with open(filePath, 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Common Name', 'Scientific Name', 'Status', 'Number', 'Number Back'])

    for bird in birds:
        attrs = bird.find_all('td')
        details = list()
        for i in range(5):
            if len(attrs[i].get_text()) < 1:
                details.append('living') # handling species that are still living
            else:
                details.append(attrs[i].get_text().strip())
        writer.writerow(details)

csvFile.close()
print("Operation Complete!")

# Fetch data from the API and generate a csv file for the bird species, family and more
import requests 
import csv, os

response = requests.get("https://xeno-canto.org/api/2/recordings?query=cnt:uganda")

if response.status_code == 200:
    data = response.json()
    recordings = data['recordings']

    directory = os.getcwd()
    filePath = os.path.join(directory, 'birdSongs.csv')
    
    with open(filePath, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['Gen', 'Species', 'English Name', 'Recordist', 'Country', 'Location', 'Type', 'Length', 'Date Uploaded', 'Remarks'])

        for recording in recordings:
            details = [recording['gen'], recording['sp'], recording['en'], recording['rec'], recording['cnt'], recording['loc'], recording['type'], recording['length'], recording['uploaded'], recording['rmk']]
            try:
                writer.writerow(details)
            except UnicodeEncodeError:
                pass
    csvFile.close()
    print("Operation Complete!")
else:
    print("Failed to establish connection")