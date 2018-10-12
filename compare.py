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
            teams = row.split(' at ')

            team_1 = teams[0]
            team_2 = teams[1].split(',')

            print(team_1)
            print(team_2[0])
            print('\n')

        return schedule_spread, team_1, team_2[0]


if __name__ == "__main__":
    print(schedule_spread_teams())
