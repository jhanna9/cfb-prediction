from bs4 import BeautifulSoup
from statistics import mean, stdev
import csv
import itertools as it
import os
import re
import requests

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}

# global path variables 
# my_path = 'C:/Users/Jim/Documents/+programming/cfb-prediction/stat_csv/' # for deskop
my_path = 'C:/Users/J/Documents/python/cfb-prediction/stat_csv' # for laptop
# data = 'http://www.covers.com/Sports/NCAAF/Odds/US/SPREAD/competition/Online/ML' # for schedule
spreads = 'https://www.covers.com/sports/ncaaf/matchups'


def stat_num_reader(text_file):
	'''Reads a text file

	text_file = the file to be read

	returns a generator object

	'''
	with open(text_file, 'r') as f:
		for line in f.readlines():
			stat_name, stat_page_num  = line.split()

			yield stat_name, stat_page_num


def build_stat_page_links():
	'''Builds links to all relevant NCAA football statistics

	returns a list

	'''
	# list to return
	stat_page_link = []

	# the standard prefix for each statistic
	link = 'http://www.ncaa.com/stats/football/fbs/current/team/'

	# each stat has 3 pages of teams/stats
	more_pgs = ['', '/p2', '/p3']

	# stat and page number tuples
	stat_page = list(stat_num_reader('stat_num.txt'))

	h = 0

	# creating links to stat pages  
	for stat in stat_page:
		for pgs in more_pgs: # creating a new link for 3 pages per stat
			page_link = link + str(stat_page[h][1]) + pgs

			stat_page_link.append(page_link)
		h += 1

	return stat_page_link


def site_to_csv(links):
	'''Scrapes all links to important stats and saves them to a csv file

	returns a string

	'''
	# get stat name to use as csv file name
	csv_name = list(stat_num_reader('stat_num.txt'))
	for name in csv_name:
		file_name = str(name[0]) + '.csv'
		count = 0

		# new csv file opened per stat
		with open(os.path.join(my_path, file_name), 'w', newline='') as f:
			file_writer = csv.writer(f)
			
			# makes sure that all three pages of stat data is pulled from site
			while count < 3:
				address = requests.get(links[0], headers=headers) # get site info using requests

				# removes first link from links ensuring that a new link is added to the csv
				del links[0]

				# create BeautifulSoup object to pull out data
				soup = BeautifulSoup(address.content, 'html.parser')
				soup_table = soup.table # grab table from page

				# count to write headers to csv after 1 loop only
				rows = 0

				# grab all table rows for data
				for tr in soup_table.find_all('tr'):
					# find table headers and data
					th = tr.find_all('th')
					td = tr.find_all('td')

					# headers are written to csv from the first page only
					if rows < 1 and count == 0:
						file_writer.writerow([elem.text.strip() for elem in th]) # strips header data from text
						rows += 1
					# used to skip the first blank line in the table data pull
					elif rows == 0: 
						rows += 1
					else:
						file_writer.writerow([elem.text.strip() for elem in td]) # strips table data from text

				count += 1

	finished = 'The CSV files are finished and located here: ' + my_path

	# return path to new csv files
	return finished


def teams(data):
	'''Scrapes Covers site for current weekly schedule

	returns a list

	'''
	teams = []

	address = requests.get(data, headers=headers)
	soup = BeautifulSoup(address.content, 'html.parser')

	for span in soup.find_all('div', class_='cmg_matchup_header_team_names'):  # cover-CoversOdds-tableTeamLink'):
		teams.append(span.text.strip())

	return teams


def chunks(l, n):
	'''https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks

	Yield successive n-sized chunks from l

	'''
	for i in range(0, len(l), n):
		yield l[i:i + n]


def schedule_csv(teams, point_spread):
	'''Writes a list of teams based on current schedule to a csv file

	returns a string

	'''
	with open(os.path.join(my_path, 'schedule_spread.csv'), 'w', newline='') as f:
		file_writer = csv.writer(f)

		# writes one away team, one home team, one spread per row
		i = 0
		for row in teams:
			new_row = (row[0], row[1], point_spread[i])
			file_writer.writerow(new_row)
			i += 1

	finished = 'The CSV file is finished and located here: ' + my_path

	return finished


def spread(link):
    '''Takes a URL input and scrapes for current spread

    Keyword arguments:
    link -- url to game schedule

    returns: a list
    '''
    # list to return
    spread_lst = []

    # pull data from site and create BS object
    spread = requests.get(link, headers=headers)
    soup = BeautifulSoup(spread.content, 'html.parser')

    # iterate through BS object looking for div and class='cmg_matchup_list_home_odds'
    for tag in soup.find_all('div', class_='cmg_matchup_list_home_odds'):
    	t = tag.text.strip()
    	spread_lst.append(t[0:5])

    return spread_lst


# function calls
# print(site_to_csv(build_stat_page_links()))
# print(passes_int_clean('Passes_Intercepted.csv'))
# print((list(csv_stat_calc())))
print(teams(spreads))
# two_teams = list(chunks(teams, 2))
print(spread(spreads))
# schedule_csv(two_teams, pt_spreads)

# prints out covers' spread in good format
# x = 1
# for s in spread(spreads):
#     sprd = s[0:5]
#     print(s[0:5])
#     print(type(sprd))
#     for n in sprd:
#     	print(n)
#     x += 1
#     if x == 4:
#     	break
#     # print('a')
#     # print('\n')
