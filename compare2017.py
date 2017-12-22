from data_pull import stat_num_reader
from scipy import stats
import csv
import os

def stat_array(stat_position_file):
	'''


	'''
	my_path = 'C:/Users/Jim/Documents/+programming/cfb-prediction/stat_csv'
	# out_path = 'C:/Users/Jim/Documents/+programming/cfb-prediction/stat_csv/z_scores'

	stats = list(stat_num_reader(stat_position_file))

	for items in stats:
		csv_file = items[0] + '.csv'
		stat_list = []
		

		with open(os.path.join(my_path, csv_file), 'r') as f:
			file_reader = csv.reader(f)
			next(file_reader)

			for row in file_reader:
				stat_list.append(float(row[int(items[1])]))

		yield stat_list


def z_score_array(stat_list):
	'''


	'''
	z_score_list = []

	for s in stat_list:
		z_score_list = stats.zscore(s)

		yield z_score_list

# def csv_stat_calc():
# 	'''


# 	'''
# 	stats = list(stat_num_reader('stat_num.txt'))

# 	for name in stats:
# 		file_name = name[0] + '.csv'
# 		stat_list = []

# 		with open(os.path.join(my_path, file_name), 'r') as f:
# 			file_reader = csv.reader(f)
# 			next(file_reader)

# 			for row in file_reader:
# 				stat_list.append(float(row[-1]))

# 			stat_mean = mean(stat_list)
# 			stat_sdev = stdev(stat_list)

# 			# print(name[0], stat_mean, stat_sdev)

# 		yield name[0], stat_mean, stat_sdev


# def passes_int_clean(csv_file):
# 	'''Opens a csv file, finds the correct statistic by column, and saves a new csv file

# 	returns a string

# 	'''
# 	with open(os.path.join(my_path, csv_file), 'r') as f, open(os.path.join(my_path, 'Passes_Intercepted_new.csv'), 'w', newline='') as w:
# 		file_reader = csv.reader(f)
# 		file_writer = csv.writer(w)

# 		for row in file_reader:
# 			file_writer.writerow(row[:-2])


# 	return 'done'


# class Stats:
# 	def __init__(self, stat_name, stat_mean, stat_stdev):
# 		self.name = stat_name
# 		self.mean = stat_mean
# 		self.stdev = stat_stdev

# 	def store_calc():
# 		stat_calc = list(csv_stat_calc())

# 		# stats_class = []

# 		for s in stat_calc:
# 			name = str(s[0])
# 			name = Stats(s[0], s[1], s[2])
# 			# print('Stat: {} /nMean: {} /nStandard Deviation: {} /n'.format(name.name, name.mean, name.stdev))
# 			# stats_class.append(s)

# 			yield name.name, name.mean, name.stdev


print(list(z_score_array(stat_array('stat_position.txt'))))
# print(list(stat_array('stat_position.txt')))
# print(list(z_score_array(stat_array('stat_position.txt'))))
# statistics = list(Stats.store_calc())
# statistics = list(Stats.store_calc())
# print(statistics.name)
# for s in statistics:
# 	print(list(s))
