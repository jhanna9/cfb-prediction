'''


'''
import csv


def schedule_spread():
    '''


    '''
    with open('stat_csv/schedule_spread.csv') as f:
        matchup_spread = []
        reader = csv.reader(f)
        for row in reader:
            matchup_spread.append(row)

    return matchup_spread


if __name__ == "__main__":
    for game in schedule_spread():
        print(game[0], game[1])
        print('\n')
