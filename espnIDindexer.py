# -*- coding: utf-8 -*-
import urllib3 as ulib
from bs4 import BeautifulSoup as bs
http = ulib.PoolManager()
ids = ["ID List"]
#dak = dak = "http://www.espn.com/nfl/player/stats/_/id/1"
#page = http.request('GET', dak)
#soup = bs(page.data, "lxml")
#print(soup.title)

for x in range(1, 20):
    url = "http://www.espn.com/nfl/player/stats/_/id/" + str(x)
    page = http.request('GET', url)
    soup = bs(page.data, "lxml")
    title = soup.title
    #title.toString()

    if title.string != "<title>NFL - Players Rosters - National Football League - ESPN</title>":
        ids.append(x)
        print(x)
        print(title)
    else:
        ids.append("0")
    

print(ids)

