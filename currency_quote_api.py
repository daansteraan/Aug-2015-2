# a script to get excahnge rates - please dont steal my access key.. it's free so yuo can get your own at currencylayer

import urllib
import json

access_key = 'd983a2fac6427454187cbb33c219487e'
apiurl = 'http://apilayer.net/api/live?access_key=' 

url = apiurl + access_key
url_handler = urllib.urlopen(url)
data = url_handler.read()

try: 
	js = json.loads(data)
except: 
	js = None
	
usd_zar = js['quotes']['USDZAR']
	
print 'EURUSD: ',1/js['quotes']['USDEUR']	
print 'USDZAR: ',usd_zar
print 'EURZAR: ',1/js['quotes']['USDEUR']*usd_zar
print 'GBPZAR: ',1/js['quotes']['USDGBP']*usd_zar
