import requests
from bs4 import BeautifulSoup

# Retrieve the HTML content from a webpage
response = requests.get('https://www.example.com = response.content

# Create a Beautiful Soup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all anchor tags within the specified div
anchors = soup.find_all("div", class_="theatre-settings")[0].find_all("div", class_="dropdown-menu")[3].find_all("a")
