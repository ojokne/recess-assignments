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
