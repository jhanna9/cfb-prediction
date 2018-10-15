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
            matchup_spread.append(row)
            row = str(row)
            teams = row.split(' at ')

            team_1 = teams[0]
            team_2 = teams[1].split(',')

            if team_1[2] == '(':
                teams_list.append(team_1[6:])
            else:
                teams_list.append(team_1[2:])

            teams_list.append(team_2[0][:-1])

        for item in matchup_spread:
            print(item[0])

        for item in teams_list:
            print(item)

        return None  # matchup_spread, teams_list


if __name__ == "__main__":
    print(schedule_spread_teams())
