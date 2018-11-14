# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib3 as ulib
from bs4 import BeautifulSoup as bs
dak = "http://www.espn.com/nfl/player/stats/_/id/2577417"
http = ulib.PoolManager()
page = http.request('GET', dak)

soup = bs(page.data, "lxml")

all_tables = soup.find_all('td')
print(all_tables)
print("-------------------------------------------------------------------")

passing = soup.find('table', class_ = 'tablehead')
print(passing)