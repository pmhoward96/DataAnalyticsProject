# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:05:42 2018

@author: P-Dog
"""

#http://www.nfl.com/stats/categorystats?archive=false&conference=null&statisticCategory=PASSING&season=1932&seasonType=REG&experience=&tabSeq=0&qualified=false&Submit=Go
import urllib3 as ulib
from bs4 import BeautifulSoup as bs
http = ulib.PoolManager()

year = "http://www.nfl.com/stats/categorystats?archive=false&conference=null&statisticCategory=PASSING&season=1932&seasonType=REG&experience=&tabSeq=0&qualified=false&Submit=Go"
page = http.request('GET', year)
soup = bs(page.data, "lxml")
tables = soup.find_all("table")
#print(tables)
Cell, RK, P, T, POS, Comp, Att, Pct, AttG, Yds, Avg, YdsG, TD, Ints, First, FirstP, Lng, Twen, Fort, Sck, Rate = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
for x in range(1932, 1933):
    year = "http://www.nfl.com/stats/categorystats?archive=false&conference=null&statisticCategory=PASSING&season=" + str(x) + "&seasonType=REG&experience=&tabSeq=0&qualified=false&Submit=Go"
    page = http.request('GET', year)
    soup = bs(page.data, "lxml")
    tables = soup.find("table", class_ = "data-table1" )
    #if tables.string != "None":
        #print(x)
    
    for rows in tables.findAll("tr"):
        cells = rows.findAll("td")
        #print(cells)
        states = rows.findAll("th")
        if len(cells) == 20:
            Cell.append(cells[0].find (text=True))
            RK.append(cells[1].find (text=True))
            P.append(cells[2].find (text=True))
            T.append(cells[3].find (text=True)
            POS.append(cells[4].find(text=True))
            Att.append(cells[5].find(text=True))
            Pct.append(cells[6].find(text=True))
            AttG.append(cells[7].find(text=True))
            Yds.append(cells[8].find(text=True))
            Avg.append(cells[9].find(text=True))
            YdsG.append(cells[10].find(text=True))
            TD.append(cells[11].find(text=True))
            Ints.append(cells[12].find(text=True))
            First.append(cells[13].find(text=True))
            FirstP.append(cells[14].find(text=True))
            Lng.append(cells[15].find(text=True))
            Twen.append(cells[16].find(text=True))
            Fort.append(cells[17].find(text=True))
            Sck.append(cells[19].find(text=True))
            Rate.append(cells[20].find(text=True))
            
        