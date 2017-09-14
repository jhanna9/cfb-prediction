from bs4 import BeautifulSoup
import csv
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


def schedule_spread_csv():
	'''


	'''
	my_path = 'C:/Users/Jim/Documents/+programming/cfb-prediction/stat_csv/'
	data = 'http://www.covers.com/odds/football/college-football-odds.aspx'

	address = requests.get(data, headers=headers)

	soup = BeautifulSoup(address.content, 'html.parser')
	# div_id = soup.find_all('div', id='odds_teams')
	# td_covers = soup.find_all('td', class_='covers_top')

	for div in soup.find_all('div', id='odds_teams'):
		div_away = div.find_all('div', class_='team_away')
		div_home = div.find_all('div', class_='team_home')

		print([elem.text.strip() for elem in div_away])
		print([elem.text.strip() for elem in div_home])
	# div_spread = td_covers.find_all('div', class_='covers_bottom')

	# print(div_away.get_text())
	# print(div_home.get_text())
	# print(div_spread.get_text())

schedule_spread_csv()	


# print(site_to_csv(build_stat_page_links()))
