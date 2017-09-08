from bs4 import BeautifulSoup


def stat_num_reader():
	'''Reads stat_num.txt file

	returns a tuple

	'''
	with open('stat_num.txt', 'r') as f:
		for line in f.readlines():
			stat_name, stat_page_num  = line.split()

			yield stat_name, stat_page_num


def build_stat_page_links():
	'''Builds links to all relevant NCAA football statistics

	returns a string

	'''
	# list to return
	stat_page_link = []

	# the standard prefix for each statistic
	link = 'http://www.ncaa.com/stats/football/fbs/current/team/'

	# the suffixes to obtain 3 pages of teams/stats
	more_pgs = ['', '/p2', '/p3']

	# stat and page number tuples
	stat_page = list(stat_num_reader())

	h = 0

	for stat in stat_page:
		for pgs in more_pgs:
			page_link = link + str(stat_page[h][1]) + pgs

			stat_page_link.append(page_link)
		h += 1

	return stat_page_link


print(build_stat_page_links())
