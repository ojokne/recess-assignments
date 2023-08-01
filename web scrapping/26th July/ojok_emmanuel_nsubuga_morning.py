# Introduction to web scraping using BeautifulSoup
"""
- Extract information from a website using BeautifulSoup and 
parsing the HTML and XML code of the web page

# install BeautifulSoup
pip install beautifulsoup4

# import libraries
from bs4 import BeautifulSoup
import requests

url = 'https://xeno-canto.org'
"""

from bs4 import BeautifulSoup
import requests

url = 'https://xeno-canto.org'

response = requests.get(url)

# get title of the website

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('title')

print(title.text)

# Today's assignments A12
# extract all bird species from the website url https://xeno-canto.org
#  and generate a csv file for the bird species, family and more
# Extract all bird songs  from this website url https://xeno-canto.org/explore?query=cnt%3A%22Uganda%22
# use this API to get data. then end point for the website is at https://xeno-canto.org/api/2/recordings 


# jeff github email
# jeff.geoff.mis@gmail.com