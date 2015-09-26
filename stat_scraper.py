'''from bs4 import BeautifulSoup
import urllib
import re
from HTMLParser import HTMLParser

pageFile = urllib.urlopen("http://stats.ncaa.org/rankings?sport_code=MFB&division=11")
pageHtml = pageFile.read()
pageFile.close

soup = BeautifulSoup("".join(pageHtml))

#table = soup('table')

print soup.prettify() # table.prettify()
'''

import sys
from urllib import urlopen
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")
 
third_down_durl = 'http://stats.ncaa.org/rankings?sport_code=MFB&division=11'
third_down_dpage = urlopen(third_down_durl)

soup = BeautifulSoup(third_down_dpage)

for link in soup.find_all('a'):
    print(link.get('href'))


