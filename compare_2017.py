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
	my_path = 'C:/Users/Jim/Documents/+programming/cfb-prediction/stat_csv/'

	l = 0
	link = 0

	while l < len(links):
		count = 0
		
		while count < 3:
			address = requests.get(links[link], headers=headers) # get site info using requests

			# create BeautifulSoup object to pull out data
			soup = BeautifulSoup(address.content, 'html.parser')
			soup_table = soup.table # grab table from page

			stat_name_div_class = soup.find_all('div', {'class':'ncaa-stat-category-stats-title'})
			for sn in stat_name_div_class:
				stat_name_csv = sn.text.strip() + '.csv'

			print(stat_name_csv)

			with open(os.path.join(my_path, stat_name_csv), 'w', newline='') as f:
				file_writer = csv.writer(f)
				
				# count to write headers to csv after 1 loop only
				rows = 0

				for tr in soup_table.find_all('tr'):
					# find table headers and data
					th = tr.find_all('th')
					td = tr.find_all('td')

					if rows < 1:
						file_writer.writerow([elem.text.strip() for elem in th])
						rows += 1
					else:
						file_writer.writerow([elem.text.strip() for elem in td])

			count += 1

			link += 1
			print('link: ', link)
		l += 1
		print('L:', l)

	finished = 'done'

	# return path to new csv files
	return finished

print(site_to_csv(build_stat_page_links()))
