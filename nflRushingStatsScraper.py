from bs4 import BeautifulSoup as bs
import urllib3 as ulib
http = ulib.PoolManager()
year = "http://www.nfl.com/stats/categorystats?archive=true&conference=null&statisticCategory=RUSHING&season=1932&seasonType=REG&tabSeq=0&qualified=false&Submit=Go"
page = http.request('GET', year)
soup = bs(page.data, "lxml")
tables = soup.find_all("table")
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
        #print(num)
        ran = int(num)
Cell, RK, P, Team, Pos, Att, AttG, Yds, Avg, YdsG, TD, Lng, First, FirstP, Twen, Fort, Fum, Year = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[], []

for x in range(1932, 2019):
    yearNumber = x
    num = ""
    year = "http://www.nfl.com/stats/categorystats?tabSeq=0&season=" + str(x)
    yearTest = year + "&seasonType=REG&Submit=Go&experience=&archive=false&conference=null&statisticCategory=RUSHING&d-447263-p=1&qualified=true"
    page = http.request('GET', yearTest)
    soup = bs(page.data, "lxml")
    tag = soup.find_all("a")
    first = str(tag).split('>')
    for x in range(len(first)):
        tag2 = first[x].split('<')
        if tag2[0] == 'next':
            temp = first[x - 2].split('<')
            num = temp[0]
            #print(num)
            ran = int(num)
    for y in range(1, ran + 1):
        end = "&seasonType=REG&Submit=Go&experience=&archive=false&conference=null&statisticCategory=RUSHING&d-447263-p=" + str(y) + "&qualified=true"
        full = year + end
        page = http.request('GET', full)
        soup = bs(page.data, "lxml")
        tables = soup.find("table", class_ = "data-table1" )


        for rows in tables.findAll("tr"):
            cells = rows.findAll("td")
            #print(cells)
            states = rows.findAll("th")
            if len(cells) == 16:
                #Cell.append(cells[0].find (text=True))
                RK.append(cells[0].find (text=True))
                P.append(cells[1].find (text=False))
                Team.append(cells[2].find (text=False))
                Pos.append(cells[3].find (text=True))
                Att.append(cells[4].find (text = True))
                AttG.append(cells[5].find (text=True))
                Yds.append(cells[6].find (text=True))
                Avg.append(cells[7].find(text=True))
                YdsG.append(cells[8].find(text=True))
                TD.append(cells[9].find(text=True))
                Lng.append(cells[10].find(text=True))
                First.append(cells[11].find(text=True))
                FirstP.append(cells[12].find(text=True))
                Twen.append(cells[13].find(text=True))
                Fort.append(cells[14].find(text=True))
                Fum.append(cells[15].find(text=True))
                Year.append(yearNumber)
                
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

#Parsing Att
for i in range(len(Att)):
    x = str(Att[i]).strip()
    Att[i] = x

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

#Parsing Fum
for i in range(len(Fum)):
    x = str(Fum[i]).strip()
    Fum[i] = x

#Parsing First
for i in range(len(First)):
    x = str(First[i]).strip()
    First[i] = x

#Parsing FirstP
for i in range(len(FirstP)):
    x = str(FirstP[i]).strip()
    FirstP[i] = x

#print(P, Team)

import pandas as pd
df = pd.DataFrame(Year, columns = ['Year'])
df['Player Name'] = P
df['Team Name'] = Team
df['Position'] = Pos
df['Rushing Attempts'] = Att
df['Rushing Attempts Per Game'] = AttG
df['Rushing Yards'] = Yds
df['Average Rushing Yards Gained'] = Avg
df['Rushing Yards Per Game'] = YdsG
df['Rushing Touchdowns'] = TD
df['Longest Rushing Play'] = Lng
df['Rushing First Downs'] = First
df['Rushing First Down Percentage'] = FirstP
df['Passing Plays over 20 Yards'] = Twen
df['Passing Plays over 40 Yards'] = Fort
df['Fumbles'] = Fum

print(df.head())
print(df)
filename = "RushingStats.csv"
f = open(filename, "w+")
f.close()
df.to_csv(r'C:\Users\P-Dog\Documents\GitHub\DataAnalyticsProject\RushingStats.csv')





