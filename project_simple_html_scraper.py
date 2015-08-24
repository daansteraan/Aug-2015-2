
"""
Create an application which connects to a site and pulls out all links, \
or images, and saves them to a list.

ADD - links to IOL.co.za and pulls out all the latest political news links, \
appending them to news_unique.

Script can be modified so that the user can choose his category of news

"""

from bs4 import BeautifulSoup as bs
import requests

links = []
news = []
page = requests.get('http://www.iol.co.za/news')

data = page.text

soup = bs(data)

print soup.title.string
print 

for link in soup.find_all('a'):   
    links.append(link.get('href'))
    
for link in links:
    if link[:37] == 'http://www.iol.co.za:80/news/politics':
        news.append(link)
        
news_unique = set(news)

print "*** NEWS LINKS / politics ***"
print
for link in news_unique:
    print link
        
print
print " *************"
print "DONE"

