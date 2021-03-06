from bs4 import BeautifulSoup
# from statistics import mean, stdev
import csv
# import itertools as it
import os
# import re
import requests

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}

# global path variables
my_path = 'C:/Users/J/Documents/python/cfb-prediction/stat_csv'  # for laptop
data = 'https://www.covers.com/sports/ncaaf/matchups'


def stat_num_reader(text_file):
    '''Reads a text file

    text_file = the file to be read
    returns a generator object

    '''
    with open(text_file, 'r') as f:
        for line in f.readlines():
            stat_name, stat_page_num = line.split()

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
        for pgs in more_pgs:  # creating a new link for 3 pages per stat
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
                address = requests.get(links[0], headers=headers)  # get site info using requests

                # removes first link from links ensuring that a new link is added to the csv
                del links[0]

                # create BeautifulSoup object to pull out data
                soup = BeautifulSoup(address.content, 'html.parser')
                soup_table = soup.table  # grab table from page

                # count to write headers to csv after 1 loop only
                rows = 0

                # grab all table rows for data
                for tr in soup_table.find_all('tr'):
                    # find table headers and data
                    th = tr.find_all('th')
                    td = tr.find_all('td')

                    # headers are written to csv from the first page only
                    if rows < 1 and count == 0:
                        file_writer.writerow([elem.text.strip() for elem in th])  # strips header data from text
                        rows += 1
                    # used to skip the first blank line in the table data pull
                    elif rows == 0:
                        rows += 1
                    else:
                        file_writer.writerow([elem.text.strip() for elem in td])  # strips table data from text

                count += 1

    finished = 'The CSV files are finished and located here: ' + my_path

    # return path to new csv files
    return finished


def schedule(sched):
    '''Scrapes Covers site for current weekly schedule

    returns a list

    '''
    teams = []

    address = requests.get(data, headers=headers)
    soup = BeautifulSoup(address.content, 'html.parser')

    for span in soup.find_all('div', class_='cmg_matchup_header_team_names'):  # cover-CoversOdds-tableTeamLink'):
        teams.append(span.text.strip())

    return teams


def spread_content(link):
    '''Takes a URL input and scrapes Covers live team odds

    Keyword arguments:
    link -- url to game schedule

    returns: a list
    '''
    # list to return
    spread_scrape = []

    # pull data from site and create BS object
    spread = requests.get(link, headers=headers)
    soup = BeautifulSoup(spread.content, 'html.parser')

    # iterate through BS object looking for div and class='cmg_matchup_list_home_odds'
    for tag in soup.find_all('div', class_='cmg_team_live_odds'):  # 'div', class_='cmg_matchup_list_home_odds'):
        for span in tag.find_all('span'):
            spread_scrape.append(span.text.strip())

    return spread_scrape


def spreads(sprd_scrape):
    '''Takes content scraped from spread_content() and extracts current spread


    '''
    spread_lst = []
    i = 0
    for s in sprd_scrape:
        if i == 2:
            sprd = s.split()
            spread_lst.append(sprd[1])
            i = 0
        else:
            i += 1

    return spread_lst


def schedule_csv(sched_spread):
    '''Writes a list of teams based on current schedule to a csv file

    returns a string

    '''
    with open(os.path.join(my_path, 'schedule_spread.csv'), 'w', newline='') as f:
        file_writer = csv.writer(f)

        # writes one game and one spread per row
        for row in sched_spread:
            file_writer.writerow(row)

    finished = 'The CSV file is finished and located here: ' + my_path

    return finished


def main():
    # pulls all current stats and writes them to csvs
    print(site_to_csv(build_stat_page_links()))

    # gets schedule/spread for upcoming games and writes them to a csv
    # schedule_spread = zip(schedule(data), spreads(spread_content(data)))
    # print(schedule_csv(schedule_spread))


if __name__ == '__main__':
    main()
