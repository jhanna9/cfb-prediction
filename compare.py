'''


'''
import csv


def schedule_spread_teams():
    '''

    '''
    with open('stat_csv/schedule_spread.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            row = str(row)
            schedule_spread = row
            teams = row.split()

            # need to figure out teams with top 25 rankings
            if len(teams) == 6:
                team_1 = teams[0] + ' ' + teams[1]
                team_2 = teams[3] + ' ' + teams[4]
            else:
                team_1 = teams[0]
                team_2 = teams[2]

            print(team_1)
            print(team_2)
            print('\n')

        # return schedule_spread, team_1, team_2


if __name__ == "__main__":
    print(schedule_spread_teams())
