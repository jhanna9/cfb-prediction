from urllib import urlopen
from bs4 import BeautifulSoup

covers = 'http://www.covers.com/pageLoader/pageLoader.aspx?page=/data/ncf/statistics/2015-2016/defense_yards.html'

cov = urlopen(covers)

soup = BeautifulSoup(cov)

print soup.prettify() # find_all('table')
