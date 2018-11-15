# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:05:42 2018

@author: P-Dog
"""

#http://www.nfl.com/stats/categorystats?archive=false&conference=null&statisticCategory=PASSING&season=1932&seasonType=REG&experience=&tabSeq=0&qualified=false&Submit=Go
import urllib3 as ulib
from bs4 import BeautifulSoup as bs
http = ulib.PoolManager()

year = "http://www.nfl.com/stats/categorystats?tabSeq=0&season=1932&seasonType=REG&Submit=Go&experience=&archive=false&conference=null&statisticCategory=PASSING&d-447263-p=1&qualified=true"
page = http.request('GET', year)
soup = bs(page.data, "lxml")
tables = soup.find_all("table")
#print(tables)
Cell, RK, P, Team, Pos, Comp, Att, Pct, AttG, Yds, Avg, YdsG, TD, Ints, First, FirstP, Lng, Twen, Fort, Sck, Rate, Year = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
for y in range(1,3):
    end = "&seasonType=REG&Submit=Go&experience=&archive=false&conference=null&statisticCategory=PASSING&d-447263-p=" + str(y) + "&qualified=true"
    for x in range(1932, 2019):
        year = "http://www.nfl.com/stats/categorystats?tabSeq=0&season=" + str(x) + end
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
                #Cell.append(cells[0].find (text=True))
                RK.append(cells[0].find (text=True))
                P.append(cells[1].find (text=False))
                Team.append(cells[2].find (text=False))
                Pos.append(cells[3].find (text=True))
                Comp.append(cells[4].find (text = True))
                Att.append(cells[5].find (text=True))
                Pct.append(cells[6].find (text=True))
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
                Sck.append(cells[18].find(text=True))
                Rate.append(cells[19].find(text=True))
                Year.append(x)
            
           
                
 #Parsing Player Names
for i in range(len(P)):
    start = str(P[i]).find('>')
    s = '>'
    end = start
    while(s != '<'):
        end = end + 1
        s = str(P[i])[end]
    sub = str(P[i])[start+1: end]  
    P[i] = sub    
#Parsing Team Names
for i in range(len(Team)):
    subs = str(Team[i]).split('/')
    if subs[0] == 'None':
        Team[i] = 'NA'
    else:
        Team[i] = subs[2]
#Parsing Comp
for i in range(len(Comp)):
    x = str(Comp[i]).strip()
    Comp[i] = x
#Parsing Att
for i in range(len(Att)):
    x = str(Att[i]).strip()
    Att[i] = x
#Parsing Pct
for i in range(len(Pct)):
    x = str(Pct[i]).strip()
    Pct[i] = x
#Parsing AttG
for i in range(len(AttG)):
    x = str(AttG[i]).strip()
    AttG[i] = x
#Parsing Yards
for i in range(len(Yds)):
    x = str(Yds[i]).strip()
    Yds[i] = x
#Parsing Avg
for i in range(len(Avg)):
    x = str(Avg[i]).strip()
    Avg[i] = x
#Parsing YdsG
for i in range(len(YdsG)):
    x = str(YdsG[i]).strip()
    YdsG[i] = x
#Parsing TD
for i in range(len(TD)):
    x = str(TD[i]).strip()
    TD[i] = x
#Parsing Ints
for i in range(len(Ints)):
    x = str(Ints[i]).strip()
    Ints[i] = x
#Parsing First
for i in range(len(First)):
    x = str(First[i]).strip()
    First[i] = x
#Parsing FirstP
for i in range(len(FirstP)):
    x = str(FirstP[i]).strip()
    FirstP[i] = x
#Parsing Lng
for i in range(len(Lng)):
    x = str(Lng[i]).strip()
    Lng[i] = x
#Parsing Twen
for i in range(len(Twen)):
    x = str(Twen[i]).strip()
    Twen[i] = x
#Parsing Fort
for i in range(len(Fort)):
    x = str(Fort[i]).strip()
    Fort[i] = x
#Parsing Sck
for i in range(len(Sck)):
    x = str(Sck[i]).strip()
    Sck[i] = x
#Parsing Rate
for i in range(len(Rate)):
    x = str(Rate[i]).strip()
    Rate[i] = x



import pandas as pd
df = pd.DataFrame(Year, columns=['Year'])
df['Player Name'] = P
df['Team Name'] = Team
df['Position'] = Pos
df['Completions'] = Comp
df['Attempts'] = Att
df['Completion Percentage'] = Pct
df['Attempts Per Game'] = AttG
df['Passing Yards'] = Yds
df['Average Yards Gained'] = Avg
df['Yards Per Game'] = YdsG
df['Touchdowns'] = TD
df['Interceptions'] = Ints
df['First Downs'] = First
df['First Down Percentage'] = FirstP
df['Longest Play'] = Lng
df['Plays over 20 Yards'] = Twen
df['Plays over 40 Yards'] = Fort
df['Sacks'] = Sck
df['Quaterback Rating'] = Rate

print(df.head())
filename = "PassingStats.csv"
f = open(filename, "w+")
f.close()
df.to_csv(r'C:\Users\P-Dog\Documents\GitHub\DataAnalyticsProject\PassingStats.csv')