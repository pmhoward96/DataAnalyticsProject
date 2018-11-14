# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:22:11 2018

@author: duke8
"""

import urllib3
from bs4 import BeautifulSoup as bs
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
http = ulib.PoolManager()
page = http.request('GET', wiki)

soup = bs(page.data, "lxml")


all_tables=soup.find_all('table')
print(all_tables)