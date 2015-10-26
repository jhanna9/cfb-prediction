# a script that compares stats and picks winners ats
# imports
from link_builder import build_link
from schedule_spread import *
from sos_strk import *
from stat_scraper import *


# file that contains numeric code for each stat 
f = open('stat_value.txt', 'r')

# generic link that the stat code is attached to
x = raw_input("Enter 'ranking_period' for up-to-date stats(ie current period = 28.0. Add 3 per week for current stats): ") 
link = 'http://stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=' + str(x) + '&amp;sport_code=MFB&amp;stat_seq='

# dictionary to store individual stats links
stat_link = {}

# build stat links
stat_link = build_link(f, link)

