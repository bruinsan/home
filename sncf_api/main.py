# import urllib2, base64
# import bs4 as BeautifulSoup
# import sys
# import unicodedata
#
# request = urllib2.Request('http://api.transilien.com/gare/87393173/depart/87393058')
# base64string = base64.encodestring('%s:%s' % ("XXX", "XXXXX")).replace('\n', '')
# request.add_header("Authorization", "Basic %s" % base64string)
# xml = urllib2.urlopen(request).read()

# import urllib2, base64
# request = urllib2.Request("http://api.foursquare.com/v1/user")
# 1bbd8684-134b-4c5c-a89d-0730e531cdfa
# request = urllib2.Request("https://api.sncf.com/v1")
# base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
# request.add_header("Authorization", "Basic %s" % base64string)
# result = urllib2.urlopen(request)

#
# soup = BeautifulSoup.BeautifulSoup(xml, "xml")
# #for tag in soup.find_all(class_='heure_train'):
# for train in soup.find_all("train"):
# 	for date in train.find_all("date"):
# 		toSend += ' '+ date.string[11:16]
# 	for etat in train.find_all("etat"):
# 		toSend += etat.string[0:1]
# toSend += '"}'
#
# print(toSend)

import requests
import pprint

token_auth="1bbd8684-134b-4c5c-a89d-0730e531cdfa"

url_avec_params='https://api.sncf.com/v1/coverage/sncf/stop_areas'

# url_avec_params='https://api.sncf.com/v1/coverage/'
r=requests.get(url_avec_params,auth=(token_auth,''))
pprint.pprint(r.json())
