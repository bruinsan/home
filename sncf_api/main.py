# -*- coding: utf-8 -*-
import requests
import pprint
from datetime import datetime, timedelta
import time
import os

import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)



def date_scnf_to_human(chaine) :
    ''' from sncf date format to readable format'''
    return datetime.strptime(chaine.replace('T',''),'%Y%m%d%H%M%S')

def date_human_to_sncf(dt) :
    ''' date time to string format for sncf api'''
    return datetime.strftime(dt, '%Y%m%dT%H%M%S')

now = datetime.now()
now_sncf = date_human_to_sncf(now)

# https://api.navitia.io/v1/journeys?from={resource_id_1}&to={resource_id_2}&datetime={date_time_to_leave}
# u'https://api.sncf.com/v1/coverage/sncf/lines/{lines.id}/departures
# u'https://api.sncf.com/v1/coverage/sncf/lines/{lines.id}/arrivals
# url_avec_params='https://api.sncf.com/v1/coverage/sncf/lines'
# url_avec_params = 'https://api.sncf.com/v1/coverage/sncf/stop_areas'

# url_avec_params='https://api.sncf.com/v1/coverage/sncf/stop_points/stop_point:' \
#                 'OCE:SP:TGV-87686006/departures?from_datetime={}'.format(now_sncf)

# pprint.pprint(r.json())
# stop_area:OCE:SA:87686006 - Paris-Gare-de-Lyon
# stop_area:OCE:SA:87681247 - Le Vert-de-Maisons
token_auth="1bbd8684-134b-4c5c-a89d-0730e531cdfa"
''' GETTING ALL STOPS AVAILABLE ON API
for stop_points_page in xrange(1,122):
    time.sleep(5)
    url_avec_params = 'https://api.sncf.com/v1/coverage/sncf/stop_areas?start_page={}'.format(stop_points_page)
    r=requests.get(url_avec_params,auth=(token_auth,''))

    # file_name = os.path.join(os.environ["HOME"],"","","gare_page_{}".format(stop_points_page))
    file_name = os.path.join(os.getcwd(),"gares_page","gare_page_{}".format(stop_points_page))
    with open(file_name, 'w') as fl:
        for gares in r.json()['stop_areas']:
            fl.write("name: {}  |   id: {}\n".format(gares['name'].encode('utf-8'), gares['id'].encode('utf-8')))
'''
home = "stop_area:OCE:SA:87681247"
lyon = "stop_area:OCE:SA:87686006"
url_avec_params = 'https://api.sncf.com/v1/coverage/sncf/journeys?from={}&to={}&datetime={}'.format(home, lyon, now_sncf)
r=requests.get(url_avec_params,auth=(token_auth,''))

time_departure =  r.json()['journeys'][0]['departure_date_time']
time_arrival =  r.json()['journeys'][0]['arrival_date_time']

print "Your train leaves at: {} and arrives at: {}".format(date_scnf_to_human(time_departure), date_scnf_to_human(time_arrival))

url_avec_params = 'https://api.sncf.com/v1/coverage/sncf/journeys?from={}&to={}&datetime={}'.format(home, lyon, time_arrival)
r=requests.get(url_avec_params,auth=(token_auth,''))

time_next_departure =  r.json()['journeys'][0]['departure_date_time']
time_next_arrival =  r.json()['journeys'][0]['arrival_date_time']

print "The next train leaves at: {} and arrives at: {}".format(date_scnf_to_human(time_next_departure), date_scnf_to_human(time_next_arrival))

# Mbox('Train HOME-PARIS', str(date_scnf_to_human(time_departure)), 1)
# import IPython
# IPython.embed()
