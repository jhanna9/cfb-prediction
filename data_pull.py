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
my_path = 'C:/Users/Jim/Documents/+programming/cfb-prediction/stat_csv/' # for deskop
# my_path = 'C:/Users/J/Documents/python/cfb-prediction/stat_csv' # for laptop
data = 'http://www.covers.com/Sports/NCAAF/Odds/US/SPREAD/competition/Online/ML' # for schedule/spread
# http://www.covers.com/Sports/NCAAF/Odds/1

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


def teams():
	'''



	'''
	teams = []

	address = requests.get(data, headers=headers)
	soup = BeautifulSoup(address.content, 'html.parser')

	for span in soup.find_all('span', class_='cover-CoversOdds-tableTeamLink'):
		teams.append(span.text.strip())

	return teams


def chunks(l, n):
	'''https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks


	Yield successive n-sized chunks from l
	'''
	for i in range(0, len(l), n):
		yield l[i:i + n]


def schedule_csv(teams):
	'''Joins lists of teams and spreads into one list and writes each line to a csv


	returns a string

	'''
	with open(os.path.join(my_path, 'schedule_spread.csv'), 'w', newline='') as f:
		file_writer = csv.writer(f)

		# writes one away team, one home team, one spread per row
		for row in teams:
			new_row = (row[0], row[1])
			file_writer.writerow(new_row)

	finished = 'The CSV file is finished and located here: ' + my_path

	return finished


def csv_stat_calc():
	'''


	'''
	stats = list(stat_num_reader('stat_num.txt'))

	for name in stats:
		file_name = name[0] + '.csv'
		stat_list = []

		with open(os.path.join(my_path, file_name), 'r') as f:
			file_reader = csv.reader(f)
			next(file_reader)

			for row in file_reader:
				stat_list.append(float(row[-1]))

			stat_mean = mean(stat_list)
			stat_sdev = stdev(stat_list)

			# print(name[0], stat_mean, stat_sdev)

		yield name[0], stat_mean, stat_sdev


def passes_int_clean(csv_file):
	'''


	'''
	with open(os.path.join(my_path, csv_file), 'r') as f, open(os.path.join(my_path, 'Passes_Intercepted_new.csv'), 'w', newline='') as w:
		file_reader = csv.reader(f)
		file_writer = csv.writer(w)

		for row in file_reader:
			file_writer.writerow(row[:-2])


	return 'done'


# print(site_to_csv(build_stat_page_links()))
# print(passes_int_clean('Passes_Intercepted.csv'))
# print((list(csv_stat_calc()))
teams = teams()
two_teams = list(chunks(teams, 2))
schedule_csv(two_teams)