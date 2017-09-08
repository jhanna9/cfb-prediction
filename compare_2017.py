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


# print(build_stat_page_links())


def site_to_csv(links):
	'''Scrapes all links to important stats and saves them to a csv file

		returns a string

	'''
	my_path = 'C:/Users/Jim/Documents/+programming/cfb-prediction/stat_csv/'

	with open(os.path.join(my_path, 'stat_1.csv'), 'w') as f:
		file_writer = csv.writer(f)
		address = requests.get(links[0], headers=headers) # get site info using requests

		soup = BeautifulSoup(address.content, 'html.parser')
		soup_table = soup.table

		for text in soup.find_all('td'):
			print(text.get_text())
			file_writer.writerow(text.get_text())

		# for row in soup_table: # .get_text():
		# 	file_writer.writerows(row)

	finished = 'done'

	return finished

	# return path to new csv files


print(site_to_csv(build_stat_page_links()))