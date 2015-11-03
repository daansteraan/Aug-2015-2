import urllib as url
import re
import time
from bs4 import BeautifulSoup as bs

# injured players
injuries_page = url.urlopen('http://www.premierinjuries.com')
injured_players = []

for line in injuries_page.readlines():
	player = re.findall('<td>(.+)</td>',line)
	if not player:
		pass
	else:
		injured_players.append(player[0].strip().split(' ')[-1])

# my team
team_page = url.urlopen('https://barxffl.com/team.aspx?page=view&id=3000659')
team = []
soup = bs(team_page)

tags = soup('span')
player_number = 1
id = 'ctl14_lblp'

for i in range(10):
	player_id = id + str(player_number)
	team.append(soup.find(id=player_id).get_text().split(' ')[-1])
	player_number+=1

print "\n --MY TEAM--\n"
for i in team:
	print i
print
	
# checking function
for player in team:
	injured = False
	if player in injured_players:
		print "%s is injured..." % player
		injured = True
		time.sleep(1)

if not injured:
	print '\nNo injuries at this time\n'
else:
	print '\nYou need to make replacements\n'
				