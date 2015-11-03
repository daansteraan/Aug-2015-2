'''
Author: Danie
Date:02/11/2015

Scraping my players from Barx FFL and Premier Injuries to see who is injured.

'''

from bs4 import BeautifulSoup as bs
import socket


#getting the injured players
source = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
source.connect(('www.premierinjuries.com',80))
source.send('GET http://www.premierinjuries.com/ HTTP/1.0\n\n')

injuries_page = ''

while True:
    data = source.recv(512)
    if not data:
        break
    injuries_page += data

source.close()

injuries_soup = bs(injuries_page)
inj_tag = injuries_soup('td')

for player in inj_tag:
    print player.get_text()


# getting my players from Barx
'''
barx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
barx.connect(('www.barxffl.com',80))
barx.send('GET https://barxffl.com/team.aspx?page=view&id=3000659 HTTP/1.0\n\n')

players_page = ''

while True:
    data = barx.recv(512)
    if not data:
        break
    players_page += data

barx.close()

print players_page

players_soup = bs(players_page)
pla_tag = players_soup('td')

for player in pla_tag:
    print player.get_text()
'''