# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:26:08 2018

@author: P-Dog
"""

import urllib3 as ulib
from bs4 import BeautifulSoup as bs
http = ulib.PoolManager()
year = "http://www.nfl.com/stats/categorystats?archive=true&conference=null&statisticCategory=RUSHING&season=2018&seasonType=REG&tabSeq=0&qualified=false&Submit=Go"
page = http.request('GET', year)
soup = bs(page.data, "lxml")
#print(soup.prettify)

num = ""
temp = ""
#while temp != "next":
 #   num = temp
tag = soup.find_all("a")
first = str(tag).split('>')
for x in range(len(first)):
    tag2 = first[x].split('<')
    if tag2[0] == 'next':
        temp = first[x - 2].split('<')
        num = temp[0]
#print(first)
    

print(num)
    
    




