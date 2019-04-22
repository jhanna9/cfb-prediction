'''


'''
import csv
import pandas as pd


stat_file = 'C:\\Users\\J\\Documents\\python\\cfb-prediction\\stat_csv\\Rushing_Defense.csv'


def schedule_spread():
    '''reads the schedule/spread csv and pulls out individual teams


    '''
    with open('stat_csv/schedule_spread.csv') as f:
        matchup_spread = []
        reader = csv.reader(f)
        for row in reader:
            # matchup_spread.append(row)
            if ' vs ' in row[0]:
                for col in row[0].split(' vs '):
                    print(remove_rank(col))
            else:
                for col in row[0].split(' at '):
                    print(remove_rank(col))

            print('\n')

    return matchup_spread


def remove_rank(ranked_team):
    '''removes ranking from individual team, ignores non-ranked team

        ranked_team: a list

        returns a string

    '''
    if str(ranked_team[0]) == '(':
        no_rank = ranked_team.split(') ')
        no_rank = no_rank[1]
    else:
        no_rank = ranked_team

    return no_rank


def get_useful_stats(csv_file):
    useful_stat = pd.read_csv(csv_file)
    print(useful_stat[['YPG']])  # extracts a single column

    # for row in useful_stat:
    #     print(row)


def main():
    # for game in schedule_spread():
    #     print(game[0], game[1])
    #     print('\n')
    # schedule_spread()
    get_useful_stats(stat_file)


if __name__ == "__main__":
    main()
