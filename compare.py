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
            # matchup_spread.append(row)
            if ' vs ' in row[0]:
                for col in row[0].split(' vs '):
                    print(col)
            else:
                for col in row[0].split(' at '):
                    print(col)

            print('\n')

    return matchup_spread


if __name__ == "__main__":
    # for game in schedule_spread():
    #     print(game[0], game[1])
    #     print('\n')
    schedule_spread()
