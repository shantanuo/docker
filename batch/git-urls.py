import feedparser
import re
from bs4 import BeautifulSoup
import requests 

api_url = "https://wgykjmyt0e.execute-api.us-east-1.amazonaws.com/stage"

url = "https://towardsdatascience.com/feed"
feed = feedparser.parse(url)

for post in feed.entries:
    soup = BeautifulSoup(post.description)
    for link in soup.findAll('a'):
        if 'http' in link.get('href'):
            PARAMS = {'title':link.get('href')} 
            print (link.get('href'))
            r = requests.get(url = api_url, params = PARAMS)
            print (r.text)
