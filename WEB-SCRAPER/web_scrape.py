'''
==========================================================
WEB SCRAPER
==========================================================
A basic web scraping script using beautifulsoup to parse and display the first paragraph of wikipedia 
result of the user input


'''


import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

title = raw_input("Enter the title: ")
u = title.replace(" ", "_")
url = "https://en.wikipedia.org/wiki/"+u
r= requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
print soup.find("p").text

