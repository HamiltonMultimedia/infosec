#!/usr/local/bin/python3

"""
This is a simple web scraper that has room for improvement and growth.
"""

# Remember to PIP install requests and bs4.
import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')
url = 'https://github.com/'+github_user
req = requests.get(url)
soup = bs(req.content, 'html.parser')
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_image)