'''Depricated functions for schedule and spread.  Covers updated site rendering these useless.


'''
def away_team():
	'''Scrapes site for all away team names


	returns a list

	'''
	# list to store away team name
	away = []

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

	address = requests.get(data, headers=headers)
	soup = BeautifulSoup(address.content, 'html.parser')

	# home team names from site are in nested div class='team_home'
	for div in soup.find_all('div', id='odds_teams'):
		div_home = div.find_all('div', class_='team_home')

		# append team name to home list
		for team in div_home:
			home.append(team.text.strip()[1:])

	return home


def spread():
	'''Scrapes site for all game spreads


	returns a list

	'''
	# list to store spreads
	spr = []

	address = requests.get(data, headers=headers)
	soup = BeautifulSoup(address.content, 'html.parser')

	# spreads from site are in nested div class='covers_bottom'
	for td in soup.find_all('td', class_='covers_top'):
		div_spread = td.find_all('div', class_='covers_bottom')

		# append spreads to spr list
		for s in div_spread:
			spr.append(s.text.strip())

	return spr