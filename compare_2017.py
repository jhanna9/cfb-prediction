from bs4 import BeautifulSoup
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


def site_scrape(links):
	'''Scrapes all links to important stats and saves them to a csv file

		returns 
		
	'''
	address = requests.get(links[0], headers=headers) # get site info using requests

	soup = BeautifulSoup(address.content, 'html.parser')

	return soup.get_text()


print(site_scrape(build_stat_page_links()))