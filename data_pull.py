from bs4 import BeautifulSoup
import csv
import itertools as it
import os
import re
import requests

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}


def stat_num_reader(text_file):
	'''Reads stat_num.txt file

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
	# for deskop
	my_path = 'C:/Users/Jim/Documents/+programming/cfb-prediction/stat_csv/'

	# for laptop
	# my_path = 'C:/Users/J/Documents/python/cfb-prediction/stat_csv'

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


def away_team():
	'''Scrapes site for all away team names


	returns a list

	'''
	# list to store away team name
	away = []
	data = 'http://www.covers.com/odds/football/college-football-odds.aspx'

	address = requests.get(data, headers=headers)
	soup = BeautifulSoup(address.content, 'html.parser')

	# away team names from site are in nested div class='team_away'
	for div in soup.find_all('div', id='odds_teams'):
		div_away = div.find_all('div', class_='team_away')

		# append team name to away list
		for team in div_away:
			away.append(team.text.strip())

	return away


def home_team():
	'''Scrapes site for all home team names


	returns a list

	'''
	# list to store away team name
	home = []
	data = 'http://www.covers.com/odds/football/college-football-odds.aspx'

	address = requests.get(data, headers=headers)
	soup = BeautifulSoup(address.content, 'html.parser')

	# home team names from site are in nested div class='team_home'
	for div in soup.find_all('div', id='odds_teams'):
		div_home = div.find_all('div', class_='team_home')

		# append team name to home list
		for team in div_home:
			home.append(team.text.strip())

	return home


def spread():
	'''Scrapes site for all game spreads


	returns a list

	'''
	# list to store spreads
	spr = []
	data = 'http://www.covers.com/odds/football/college-football-odds.aspx'

	address = requests.get(data, headers=headers)
	soup = BeautifulSoup(address.content, 'html.parser')

	# spreads from site are in nested div class='covers_bottom'
	for td in soup.find_all('td', class_='covers_top'):
		div_spread = td.find_all('div', class_='covers_bottom')

		# append spreads to spr list
		for s in div_spread:
			spr.append(s.text.strip())

	return spr


def schedule_spread_csv():
	'''Joins lists of away teams, home teams, and spreads into one list and writes each line to a csv


	returns a string
	'''
	my_path = 'C:/Users/Jim/Documents/+programming/cfb-prediction/stat_csv/'
	
	with open(os.path.join(my_path, 'schedule_spread.csv'), 'w', newline='') as f:
		file_writer = csv.writer(f)

		# joins the three lists into one for csv writer
		# help from https://stackoverflow.com/questions/34761978/python-merge-3-lists-into-1-list
		teams_spread = list(it.zip_longest(away_team(), home_team(), spread()))

		# writes one away team, one home team, one spread per row
		for sched in teams_spread:
			file_writer.writerow(sched)

	finished = 'The CSV file is finished and located here: ' + my_path

	return finished


print(site_to_csv(build_stat_page_links()))
print(schedule_spread_csv())
