from bs4 import BeautifulSoup
import urllib
import re
from HTMLParser import HTMLParser

pageFile = urllib.urlopen("http://www.ncaa.com/stats/football/fbs/current/team/22")
# http://web1.ncaa.org/mfb/natlRank.jsp?year=2012&rpt=IA_teamtotdef&site=org&div=IA&dest=O")
pageHtml = pageFile.read()
pageFile.close

#team =  raw_input("Enter team name: ")
soup = BeautifulSoup("".join(pageHtml))

table = soup('table')

#print table.prettify()

def stripLink():
    x = table.find_all('a')
    for link in x:
        y = link.get('href')
        print y.strip('/football/exec/rankingSummary?year=2012&org=')
    
stripLink()

def categories():
    for x in range(11):
        c = table.find_all('th')[x]
        print str(c).strip('<th/>'),
        
def team1():
    for x in range(11):
        c = table.find_all('td')[x]
        print str(c).strip('<td/>'),

def team2():
    for x in range(11,22):
        c = table.find_all('td')[x]
        print str(c).strip('<td/>')

def spacer():
    print '\n'

#print table.find_all('td')[12]
#print table.find_all(href=re.compile("Notre Dame"))

#categories()
#spacer()
#team1()
#spacer()
#team2()

"""def catStrip():
    x = table.find_all('th')[0]
    print str(x).strip('<th/>')

catStrip()"""


    

"""this program needs the following:
   1. way to parse into table data grabbing the headers and team stats
   2. a nicely formatted output
   3. a way for user to select two teams and compare stats"""





