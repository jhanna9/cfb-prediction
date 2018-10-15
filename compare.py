'''


'''
import csv


def schedule_spread_teams():
    '''

    '''
    with open('stat_csv/schedule_spread.csv') as f:
        matchup_spread = []
        teams_list = []
        reader = csv.reader(f)
        for row in reader:
            row = str(row)
            matchup_spread.append(row)
            # teams = row.split(' at ')

            # team_1 = teams[0]
            # team_2 = teams[1].split(',')

            # teams_list.append(team_1)
            # teams_list.append(team_2[0])

            print(row)
            print(len(row))
            print('\n')
            # print(team_1)
            # print('\n')
            # print(team_2[0])

        return None  # matchup_spread, teams_list


if __name__ == "__main__":
    print(schedule_spread_teams())
